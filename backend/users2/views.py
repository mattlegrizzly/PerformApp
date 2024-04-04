from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import coreschema
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
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
    @swagger_auto_schema(
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

    @swagger_auto_schema(
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

    @swagger_auto_schema(
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

    @swagger_auto_schema(
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
    @swagger_auto_schema(tags=["Users"])
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
    permission_classes = [IsAuthenticated]

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

    @swagger_auto_schema(
        tags=["Users"],
        manual_parameters=[
            openapi.Parameter(
                "page",
                openapi.IN_QUERY,
                description="This parameter is not needed",
                type=openapi.TYPE_STRING,
                required=False,
            )
        ],
        operation_description="""
        This endpoint returns user information if the user is authenticated.

        Note: The 'page' query parameter is not applicable to this endpoint and should not be used.
        """,
    )
    @method_decorator(csrf_exempt)
    def retrieve(self, request, pk):
        try:
            user = self.get_queryset().get(pk=pk)
            serializer = UserDetailedSerializer(user)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            raise PermissionDenied

    @swagger_auto_schema(tags=["Users"])
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

    @swagger_auto_schema(tags=["Users"])
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

    @swagger_auto_schema(tags=["Users"])
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

class UsersFavExercisesViewSet(viewsets.ModelViewSet):
    permission_classes = [UserViewSetPermissions]
    queryset = UsersFavExercises.objects.all()
    serializer_class = UsersFavExercisesSerializer

class InjurieViewSet(viewsets.ModelViewSet):
    permission_classes = [UserViewSetPermissions]
    queryset = Injurie.objects.all()
    serializer_class = InjurieSerializer

class WellnessViewSet(viewsets.ModelViewSet):
    permission_classes = [UserViewSetPermissions]
    queryset = Wellness.objects.all()
    serializer_class = WellnessSerializer