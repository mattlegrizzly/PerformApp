"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import include, path
from rest_framework import routers

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from users2.views import LoginViewset, LogoutViewset, RefreshTokensViewset, RegisterViewset
from users2.views import AdminUserViewSet, UserViewSet, UsersFavExercisesViewSet, InjurieViewSet, WellnessViewSet, AdminUsersAllViewSet

from sport.views import ( SportViewSet, SportsUserViewSet)
from sport.admin_views import ( AdminSportViewSet, AdminSportsUserViewSet)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from exercise.views import (
    MaterialViewSet, 
    ExerciseViewSet, 
    ExerciseStepViewSet, 
    ExerciseMaterialViewSet, 
    ExerciseSportViewSet, 
    ExerciseZoneViewSet, 
    WorkZoneViewSet
    )

from exercise.adminviews import(
    AdminMaterialViewSet,
    AdminExerciseMaterialViewSet,
    AdminExerciseViewSet,
    AdminExerciseStepViewSet,
    AdminExerciseSportViewSet,
    AdminExerciseZoneViewSet,
    AdminWorkZoneViewSet
    )


from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = routers.DefaultRouter()
#router.register('admin/users', AdminUserViewSet, basename='user_admin')
router.register('admin/users_all', AdminUsersAllViewSet, basename='user_all')
router.register('users', UserViewSet, basename='user')
router.register('injuries', InjurieViewSet, basename="injuries") 
router.register('wellness', WellnessViewSet, basename="wellness") 
router.register('userfavexercises', UsersFavExercisesViewSet, basename='user_fav_exercices')

router.register('sports', SportViewSet, basename="sports")
router.register('admin/sports', AdminSportViewSet, basename="admin_sports")

router.register('sports_user', SportsUserViewSet, basename="sports_user")
router.register('admin/sports_user', AdminSportsUserViewSet, basename="admin_sportsUser" )

router.register('materials', MaterialViewSet, basename="materials")
router.register('admin/materials', AdminMaterialViewSet ,basename="admin_materials")

router.register('exercises', ExerciseViewSet, basename='exercices')
router.register('admin/excercies', AdminExerciseViewSet, basename='admin_exercices')


router.register('exercisesteps', ExerciseStepViewSet, basename='steps')
router.register('admin/exercices_steps', AdminExerciseStepViewSet, basename='admin_steps')

router.register('exercisematerials', ExerciseMaterialViewSet, basename='exercices_material')
router.register('admin/exercisematerials', AdminExerciseMaterialViewSet, basename='admin_exercices_material')

router.register('exercisesports', ExerciseSportViewSet, basename='exercices_sports')
router.register('admin/exercisesports', AdminExerciseSportViewSet, basename='admin_exercices_sports')

router.register('exercisezones', ExerciseZoneViewSet, basename='exercices_zone')
router.register('admin/exercisezones', AdminExerciseZoneViewSet, basename='admin_exercices_zone')

router.register('workzones', WorkZoneViewSet, basename='work_zone')
router.register('admin/workzones', AdminWorkZoneViewSet, basename='admin_work_zone')

router.register("register", RegisterViewset, basename="register")
router.register("login", LoginViewset, basename="login")
router.register("logout", LogoutViewset, basename="logout")
router.register("refresh_tokens", RefreshTokensViewset, basename="refresh_tokens")

urlpatterns = [
    path("api/", include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # url(r'^rest-auth/', include('rest_auth.urls')),
    # url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    # url(r'^account/', include('allauth.urls')),
    # url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
]
