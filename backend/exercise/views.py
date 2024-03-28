from rest_framework import viewsets
from .models import Material,Exercise,ExerciseStep,ExerciseMaterial,ExerciseSport,ExerciseZone,WorkZone
from .serializers import MaterialSerializer,ExerciseSerializer,ExerciseStepSerializer,ExerciseMaterialSerializer,ExerciseSportSerializer,ExerciseZoneSerializer,WorkZoneSerializer

class MaterialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class AdminMaterialViewSet(viewsets.ModelViewSet):
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