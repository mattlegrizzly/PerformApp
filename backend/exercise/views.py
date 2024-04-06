from rest_framework import viewsets
from .models import Material, Exercise, ExerciseStep, ExerciseMaterial, ExerciseSport, ExerciseZone, WorkZone
from .serializers import MaterialSerializer, ExerciseSerializer, ExerciseStepSerializer, ExerciseMaterialSerializer, ExerciseSportSerializer, ExerciseZoneSerializer, WorkZoneSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from rest_framework.response import Response
from rest_framework import filters, mixins, status, viewsets, pagination

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
    search_fields = ["name", "description", "materials", "sports", "zones"]

    def get_queryset(self):
        queryset = Exercise.objects.all()
        return queryset

    def get_latest(self):
        queryset = Exercise.objects.all().order_by("created_at")[:5]
        return queryset

    def list(self, request, *args, **kwargs):
        if request.query_params.get("itemsPerPage"):
            self.pagination_class.page_size = request.query_params.get("itemsPerPage")
        return super().list(request, *args, **kwargs)
    
    def latest(self, request):
        latest_recipes = self.get_latest()
        serializer = self.serializer_class(latest_recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 

    def retrieve(self, request, *args, **kwargs):
        exercise_id = self.kwargs['pk']
        steps = ExerciseStep.objects.filter(exercise_id=exercise_id)
        steps_serializer = ExerciseStepSerializer(steps, many=True)
        data = steps_serializer.data
        exercise = Exercise.objects.get(pk=exercise_id)
        exercise_serializer = self.serializer_class(exercise)
        return Response(data)
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

