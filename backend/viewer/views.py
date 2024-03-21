from django.contrib.auth.models import Group
from rest_framework import permissions, viewsets

from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters, mixins, status, viewsets, pagination
from rest_framework.decorators import action

from viewer.models import (
    Exercise
)

from viewer.serializers import (
    GroupSerializer, 
)

from viewer.serializers import (
    ExerciseSerializer
)

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

from .models import User, Sport, Material, Exercise, ExerciseStep, ExerciseMaterial, ExerciseSport, ExerciseZone, WorkZone, UsersFavExercises
from .serializers import UserSerializer, SportSerializer, MaterialSerializer, ExerciseSerializer, ExerciseStepSerializer, ExerciseMaterialSerializer, ExerciseSportSerializer, ExerciseZoneSerializer, WorkZoneSerializer, UsersFavExercisesSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SportViewSet(viewsets.ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class ExerciseStepViewSet(viewsets.ModelViewSet):
    queryset = ExerciseStep.objects.all()
    serializer_class = ExerciseStepSerializer

class ExerciseMaterialViewSet(viewsets.ModelViewSet):
    queryset = ExerciseMaterial.objects.all()
    serializer_class = ExerciseMaterialSerializer

class ExerciseSportViewSet(viewsets.ModelViewSet):
    queryset = ExerciseSport.objects.all()
    serializer_class = ExerciseSportSerializer

class ExerciseZoneViewSet(viewsets.ModelViewSet):
    queryset = ExerciseZone.objects.all()
    serializer_class = ExerciseZoneSerializer

class WorkZoneViewSet(viewsets.ModelViewSet):
    queryset = WorkZone.objects.all()
    serializer_class = WorkZoneSerializer

class UsersFavExercisesViewSet(viewsets.ModelViewSet):
    queryset = UsersFavExercises.objects.all()
    serializer_class = UsersFavExercisesSerializer