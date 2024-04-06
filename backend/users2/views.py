from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import coreschema
from drf_yasg import openapi
from rest_framework import status, mixins, viewsets
from rest_framework import permissions, viewsets
from .models import User, UsersFavExercises, Wellness, Injurie
from rest_framework.schemas import coreapi
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView
from .serializers import (
    UserSerializer,     
    UserDetailedSerializer,
    UsersFavExercisesSerializer, 
    InjurieSerializer, 
    WellnessSerializer, 
    LoginSerializer,
    LogoutSerializer,
    RefreshTokensSerializer,
    RegisterSerializer,
    SetPasswordSerializer)
from users2.permissions import UserViewSetPermissions
from rest_framework.exceptions import (
    AuthenticationFailed,
    NotAuthenticated,
    NotFound,
    ParseError,
    PermissionDenied,
    ValidationError,
)

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }

class RegisterViewset(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    @method_decorator(csrf_exempt)
    @extend_schema(
        responses={status.HTTP_201_CREATED: UserSerializer()},
        tags=["Authentication"],
    )
    def create(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            serialized_user = UserSerializer(user)

            return Response(data=serialized_user.data, status=status.HTTP_201_CREATED)

        raise ValidationError(serializer.errors, code="validation_error")

class LoginViewset(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = LoginSerializer
    queryset = User.objects.all()

    @extend_schema(
        responses={status.HTTP_202_ACCEPTED: UserSerializer()},
        tags=["Authentication"],
    )
    def create(self, request):
        if "email" not in request.data or "password" not in request.data:
            raise NotAuthenticated(
                detail="Authentication credentials were not provided",
                code="not_authenticated",
            )

        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)
        print("User ", user)

        if user is not None and user.is_authenticated:
            login(request, user)

            serialized_user = UserSerializer(user)
            auth_data = get_tokens_for_user(request.user)

            return Response(
                {"user": serialized_user.data, **auth_data},
                status=status.HTTP_202_ACCEPTED,
            )

        raise AuthenticationFailed("Invalid credentials", code="authentication_failed")

class LogoutViewset(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]

    @extend_schema(
        responses={status.HTTP_205_RESET_CONTENT: LogoutSerializer()},
        tags=["Authentication"],
    )
    def create(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            response_data = {
                "message": "Logout successful. Refresh token has been revoked."
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            raise TokenError(e)

class RefreshTokensViewset(viewsets.ViewSet, TokenRefreshView):
    serializer_class = RefreshTokensSerializer

    @extend_schema(
        responses={status.HTTP_200_OK: RefreshTokensSerializer},
        tags=["Authentication"],
    )
    def create(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

# Create your views here.
class AdminUserViewSet(viewsets.ModelViewSet):
    permission_classes = [UserViewSetPermissions]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    @extend_schema(tags=["Users"])
    @method_decorator(csrf_exempt)
    @action(detail=True, methods=["patch"])
    def set_password(self, request, pk):
        try:
            user = self.get_queryset().get(pk=pk)

            if request.user.is_authenticated:
                serializer = SetPasswordSerializer(data=request.data)

                if serializer.is_valid():
                    user.set_password(request.data.get("password"))
                    user.save()

                    return Response(
                        {"password": "This field was successfully updated"},
                        status=status.HTTP_202_ACCEPTED,
                    )

                else:
                    raise ValidationError(serializer.errors, code="validation_error")
            else:
                raise NotAuthenticated(
                    "Authentication credentials were not provided.",
                    code="not_authenticated",
                )

        except ObjectDoesNotExist:
            raise NotFound

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer

    def get_schema_fields(self, path, method):
        fields = super().get_schema_fields(path, method)

        if method.lower() == "get" and path.endswith("authenticated_infos"):
            # Remove the 'page' field for the custom endpoint
            fields = [field for field in fields if field.name != "page"]

            # Add custom fields, if needed
            fields.append(
                coreapi.Field(
                    name="custom_field",
                    required=True,
                    location="query",
                    schema=coreschema.String(),
                )
            )

        return fields

    @method_decorator(csrf_exempt)
    def get_queryset(self):
        authenticated_user = self.request.user
        queryset = User.objects.filter(email=authenticated_user)

        return queryset

    @extend_schema(
        tags=["Users"],
    )
    @method_decorator(csrf_exempt)
    def retrieve(self, request, pk):
        try:
            print(self.request.user) 
            user = self.get_queryset().get(pk=pk)
            serializer = UserDetailedSerializer(user)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            raise PermissionDenied

    @extend_schema(tags=["Users"])
    def update(self, request, pk):
        try:
            user = self.get_queryset().get(pk=pk)
            serializer = UserSerializer(user, data=request.data)

            if serializer.is_valid(raise_exception=True):
                if self.request.data.get("password") != None:
                    raise ParseError(
                        "password: This field is read-only and cannot be edited.",
                        code="validation_error",
                    )
                elif self.request.data.get("is_superuser") != None:
                    raise ParseError(
                        "is_superuser: This field is read-only and cannot be edited.",
                        code="validation_error",
                    )
                elif self.request.data.get("is_active") != None:
                    raise ParseError(
                        "is_active: This field is read-only and cannot be edited.",
                        code="validation_error",
                    )
                elif self.request.data.get("last_login") != None:
                    raise ParseError(
                        "last_login: This field is read-only and cannot be edited.",
                        code="validation_error",
                    )
                else:
                    email_exists = serializer.check_email_exists(
                        User.get_obj(user)["email"], request.data["email"]
                    )
                    if email_exists:
                        raise ValidationError(
                            "Email already exists", code="validation_error"
                        )
                    else:
                        serializer.save()

                        return Response(
                            serializer.data, status=status.HTTP_202_ACCEPTED
                        )
            else:
                raise ValidationError(serializer.errors, code="validation_error")

        except ObjectDoesNotExist:
            raise NotFound

    @extend_schema(tags=["Users"])
    def partial_update(self, request, pk):
        try:
            user = self.get_queryset().get(pk=pk)
            serializer = UserSerializer(user, data=request.data, partial=True)

            if serializer.is_valid(raise_exception=True):
                if self.request.data.get("password") != None:
                    raise ParseError(
                        "password: This field is read-only and cannot be edited.",
                        code="validation_error",
                    )
                elif self.request.data.get("is_superuser") != None:
                    raise ParseError(
                        "is_superuser: This field is read-only and cannot be edited.",
                        code="validation_error",
                    )
                elif self.request.data.get("is_active") != None:
                    raise ParseError(
                        "is_active: This field is read-only and cannot be edited.",
                        code="validation_error",
                    )
                elif self.request.data.get("last_login") != None:
                    raise ParseError(
                        "last_login: This field is read-only and cannot be edited.",
                        code="validation_error",
                    )
                else:
                    if request.data.get("email") != None:
                        email_exists = serializer.check_email_exists(
                            User.get_obj(user)["email"], request.data["email"]
                        )
                        if email_exists:
                            raise ValidationError(
                                "Email already exists", code="validation_error"
                            )
                        else:
                            serializer.save()
                            return Response(serializer.data, status=status.HTTP_200_OK)
                    else:
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                raise ValidationError(serializer.errors, code="validation_error")

        except ObjectDoesNotExist:
            raise NotFound

    @extend_schema(tags=["Users"])
    @method_decorator(csrf_exempt)
    @action(detail=True, methods=["patch"])
    def set_password(self, request, pk):
        try:
            user = self.get_queryset().get(pk=pk)

            if request.user.is_authenticated:
                serializer = SetPasswordSerializer(data=request.data)

                if serializer.is_valid():
                    user.set_password(request.data.get("password"))
                    user.save()

                    return Response(
                        {"password": "This field was successfully updated"},
                        status=status.HTTP_202_ACCEPTED,
                    )

                else:
                    raise ValidationError(serializer.errors, code="validation_error")
            else:
                raise NotAuthenticated(
                    "Authentication credentials were not provided.",
                    code="not_authenticated",
                )

        except ObjectDoesNotExist:
            raise NotFound

#------------------SPORT------------------
# Admin ViewSet
class AdminUsersAllViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        tags=['Admin - Users(all)'],
        responses={200: "OK"}
    )
    def get_queryset(self):
        queryset = Recipe.objects.all()
        return queryset
        
    @extend_schema(
        tags=['Admin - Users(all)'],
        responses={200: "OK"}
    )
    def get_latest(self):
        queryset = Recipe.objects.all().order_by("created_at")[:5]
        return queryset

    @extend_schema(
        tags=['Admin - Users(all)'],
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        if request.query_params.get("itemsPerPage"):
            self.pagination_class.page_size = request.query_params.get("itemsPerPage")
        return super().list(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Users(all)'],
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Users(all)'],
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Users(all)'],
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Users(all)'],
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Users(all)'],
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class UsersFavExercisesViewSet(viewsets.ModelViewSet):
    permission_classes = [UserViewSetPermissions, permissions.IsAdminUser]
    queryset = UsersFavExercises.objects.all()
    serializer_class = UsersFavExercisesSerializer

class InjurieViewSet(viewsets.ModelViewSet):
    permission_classes = [UserViewSetPermissions]
    queryset = Injurie.objects.all()
    serializer_class = InjurieSerializer

class WellnessViewSet(viewsets.ModelViewSet):
    permission_classes = [UserViewSetPermissions, permissions.IsAdminUser]
    queryset = Wellness.objects.all()
    serializer_class = WellnessSerializer
