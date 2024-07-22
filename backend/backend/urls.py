import os

from django.contrib import admin
from django.urls import path

from django.urls import include, path
from rest_framework import routers

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings
from django.conf.urls.static import static

from users2.views import LoginViewset, LogoutViewset, RefreshTokensViewset, RegisterViewset, PasswordChangeLogViewSet
from users2.views import AdminUserViewSet, UserViewSet, UsersFavExercisesViewSet, InjurieViewSet, WellnessViewSet, AdminUsersAllViewSet

from sport.views import ( SportViewSet, SportsUserViewSet)
from sport.admin_views import ( AdminSportViewSet, AdminSportsUserViewSet)


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
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
router.register('userfavexercises', UsersFavExercisesViewSet, basename='user_fav_exercises')

router.register('sports', SportViewSet, basename="sports")
router.register('admin/sports', AdminSportViewSet, basename="admin_sports")

router.register('sports_user', SportsUserViewSet, basename="sports_user")
router.register('admin/sports_user', AdminSportsUserViewSet, basename="admin_sportsUser" )

router.register('materials', MaterialViewSet, basename="materials")
router.register('admin/materials', AdminMaterialViewSet ,basename="admin_materials")

router.register('exercises', ExerciseViewSet, basename='exercises')
router.register('admin/exercises', AdminExerciseViewSet, basename='admin_exercises')

router.register('changelogpwd', PasswordChangeLogViewSet, basename='changelog')

router.register('exercisesteps', ExerciseStepViewSet, basename='steps')
router.register('admin/steps', AdminExerciseStepViewSet, basename='admin_steps')

router.register('exercisematerials', ExerciseMaterialViewSet, basename='exercises_material')
router.register('admin/exercisematerials', AdminExerciseMaterialViewSet, basename='admin_exercises_material')

router.register('exercisesports', ExerciseSportViewSet, basename='exercises_sports')
router.register('admin/exercisesports', AdminExerciseSportViewSet, basename='admin_exercises_sports')

router.register('exercisezones', ExerciseZoneViewSet, basename='exercises_zone')
router.register('admin/exercisezones', AdminExerciseZoneViewSet, basename='admin_exercises_zone')

router.register('workzones', WorkZoneViewSet, basename='work_zone')
router.register('admin/workzones', AdminWorkZoneViewSet, basename='admin_work_zone')

router.register("register", RegisterViewset, basename="register")
router.register("login", LoginViewset, basename="login")
router.register("logout", LogoutViewset, basename="logout")
router.register("refresh_tokens", RefreshTokensViewset, basename="refresh_tokens")

urlpatterns = [
    path("api/", include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Vérifiez la variable d'environnement DEBUG
if os.getenv("DEBUG") == "True":
    urlpatterns += [
        path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
        # Optional UI:
        path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
        path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ]