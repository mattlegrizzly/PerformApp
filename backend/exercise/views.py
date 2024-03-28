from rest_framework import viewsets
from .models import Material, Exercise, ExerciseStep, ExerciseMaterial, ExerciseSport, ExerciseZone, WorkZone
from .serializers import MaterialSerializer, ExerciseSerializer, ExerciseStepSerializer, ExerciseMaterialSerializer, ExerciseSportSerializer, ExerciseZoneSerializer, WorkZoneSerializer
from drf_yasg.utils import swagger_auto_schema

#------------------MATERIAL------------------
# List/Get ViewSet
class MaterialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

#------------------EXERCISE------------------
# List/Get ViewSet
class ExerciseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

#------------------EXERCISE_STEPS------------------
# List/Get ViewSet
class ExerciseStepViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ExerciseStep.objects.all()
    serializer_class = ExerciseStepSerializer

#------------------EXERCISE_MATERIAL------------------
# List/Get ViewSet
class ExerciseMaterialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ExerciseMaterial.objects.all()
    serializer_class = ExerciseMaterialSerializer

#------------------EXERCISE_SPORTS------------------
# List/Get ViewSet
class ExerciseSportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ExerciseSport.objects.all()
    serializer_class = ExerciseSportSerializer

#------------------EXERCISE_Zone------------------
# List/Get ViewSet
class ExerciseZoneViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ExerciseZone.objects.all()
    serializer_class = ExerciseZoneSerializer

#------------------WORKZONE------------------
# List/Get ViewSet
class WorkZoneViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WorkZone.objects.all()
    serializer_class = WorkZoneSerializer

