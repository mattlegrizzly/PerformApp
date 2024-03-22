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

from users2.views import UserViewSet, UsersFavExercisesViewSet
from sport.views import ( SportViewSet, AdminSportViewSet, SportsUserViewSet, AdminSportsUserViewSet)
from exercise.views import MaterialViewSet, AdminMaterialViewSet, ExerciseViewSet, ExerciseStepViewSet, ExerciseMaterialViewSet, ExerciseSportViewSet, ExerciseZoneViewSet, WorkZoneViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('users', UserViewSet)

router.register('sports', SportViewSet, basename="sports")
router.register('admin/sports', AdminSportViewSet, basename="admin_sports")
router.register('sports_user', SportsUserViewSet, basename="sportsUser" )
router.register('admin/sports_user', AdminSportsUserViewSet, basename="admin_sportsUser" )

router.register('materials', MaterialViewSet, basename="materials")
router.register('admin/materials', AdminMaterialViewSet ,basename="admin_materials")

router.register('exercises', ExerciseViewSet)

router.register('exercisesteps', ExerciseStepViewSet)

router.register('exercisematerials', ExerciseMaterialViewSet)

router.register('exercisesports', ExerciseSportViewSet)

router.register('exercisezones', ExerciseZoneViewSet)

router.register('workzones', WorkZoneViewSet)

router.register('userfavexercises', UsersFavExercisesViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path(
        "api/docs",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path('admin/', admin.site.urls),
    # url(r'^rest-auth/', include('rest_auth.urls')),
    # url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    # url(r'^account/', include('allauth.urls')),
    # url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
]
