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
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ViewSet
import jwt
from backend.settings import SIMPLE_JWT
from rest_framework import filters, mixins, status, viewsets, pagination

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

            # Envoi de l'e-mail avec le mot de passe
            subject = 'Welcome to Our Platform'
            recipient_list = [user.email]
            message = Mail(
                from_email='contact@grizzlyperform.app',
                to_emails=recipient_list,
                subject='Perform App Registration',
                html_content= f'Hello,\n\nYour account has been created successfully. Here are your credentials:\n\nEmail: {user.email}\nPassword: {request.data.get("password")}\n\nThank you for registering!')
            try:
                sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print('error ', e)
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

        if user is not None and user.is_authenticated:
            login(request, user)

            serialized_user = UserSerializer(user)
            auth_data = get_tokens_for_user(request.user)
            is_admin = UserDetailedSerializer(user)
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
    filter_backends = [filters.SearchFilter]
    search_fields = ["email", "first_name", 'last_name']
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

#------------------ADMIN USERS------------------
# Admin ViewSet
class AdminUsersAllViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["email", "first_name", 'last_name']
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        tags=['Admin - Users(all)'],
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        if request.query_params.get("orderBy"):
            # Appliquer l'ordre initial par id si nécessaire
            order = request.query_params.get("orderBy")
            if order == "orderByNameAsc":
                queryset = self.queryset.order_by("name")
            elif order == "orderByNameDesc":
                queryset = self.queryset.order_by("-name")
            elif order == "orderByIdAsc" or order == "default":
                queryset = self.queryset.order_by("id")
            elif order == "orderByIdDesc":
                queryset = self.queryset.order_by("-id")
            elif order == "orderByDateAsc":
                queryset = self.queryset.order_by("created_at")
            elif order == "orderByDateDesc":
                queryset = self.queryset.order_by("-created_at")
        else:
            queryset = self.queryset.order_by("id")


        # Modifier la taille de la pagination si un paramètre itemsPerPage est fourni
        if request.query_params.get("itemsPerPage"):
            self.pagination_class.page_size = request.query_params.get("itemsPerPage")

        # Filtrer le queryset
        queryset = self.filter_queryset(queryset)

        # Paginer le queryset trié
        page = self.paginate_queryset(queryset)
        
        # Si la pagination est activée, sérialiser la page paginée
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        # Sinon, sérialiser le queryset complet
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(
        tags=['Admin - Users(all)'],
        responses={200: "OK"}
    )
    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
        
    @extend_schema(
        tags=['Admin - Users(all)'],
        responses={200: "OK"}
    )
    def get_latest(self):
        queryset = User.objects.all().order_by("created_at")[:5]
        return queryset

    @extend_schema(
        tags=['Admin - Users(all)'],
        responses={200: "OK"}
    )
    @action(detail=False, methods=['get'], url_path="latest")
    def latest(self, request):
        latest_users = self.get_latest()
        serializer = self.serializer_class(latest_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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

    @extend_schema(
        tags=['Admin - Users(all)'],
        responses={200: "OK"}
    )
    @action(detail=False, methods=['get'], url_path="me")
    def get_me(self, request):
        serializer = self.serializer_class(request.user)
        auth_data = get_tokens_for_user(request.user)

        return Response(
            {"user": serializer.data, **auth_data},
            status=status.HTTP_202_ACCEPTED,
        )

#------------------USERS FAV EXERCISES------------------
# Users fav exercises ViewSet
class UsersFavExercisesViewSet(viewsets.ModelViewSet):
    permission_classes = [UserViewSetPermissions, permissions.IsAdminUser]
    queryset = UsersFavExercises.objects.all()
    serializer_class = UsersFavExercisesSerializer

    @extend_schema(
        tags=['Users Fav Exercises'],
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(
        tags=['Users Fav Exercises'],
        responses={200: "OK"}
    )
    @action(detail=False, methods=['get'], url_path="latest")
    def latest(self, request):
        latest_sports_user = self.get_latest()
        serializer = self.serializer_class(latest_sports_user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        tags=['Users Fav Exercises'],
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Users Fav Exercises'],
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Users Fav Exercises'],
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Users Fav Exercises'],
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Users Fav Exercises'],
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

#------------------USERS INJURIES------------------
# Users Injuries ViewSet
class InjurieViewSet(viewsets.ModelViewSet):
    permission_classes = [UserViewSetPermissions]
    queryset = Injurie.objects.all()
    serializer_class = InjurieSerializer

#------------------USERS WELLNESS------------------
# Users Wellness ViewSet
class WellnessViewSet(viewsets.ModelViewSet):
    permission_classes = [UserViewSetPermissions, permissions.IsAdminUser]
    queryset = Wellness.objects.all()
    serializer_class = WellnessSerializer
