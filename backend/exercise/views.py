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
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "materials__name", "sports__name"]

    def get_queryset(self):
        queryset = Exercise.objects.all()
        return queryset

    def get_latest(self):
        queryset = Exercise.objects.all().order_by("created_at")[:5]
        return queryset

    def list(self, request, *args, **kwargs):
        # Appliquer l'ordre initial par id si nécessaire
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

        # Filtrer le queryset en fonction des paramètres de la requête
        material_ids = request.query_params.getlist('material_id')
        sport_ids = request.query_params.getlist('sport_id')
        workzone_codes = request.query_params.getlist('workzone_code')

        # Si des identifiants de matériaux sont fournis dans la requête
        if material_ids:
            material_ids = [int(id) for ids in material_ids for id in ids.split(',')]
            queryset = self.queryset.filter(material_exercise__material__id__in=material_ids)
        if sport_ids:
            sport_ids = [int(id) for ids in sport_ids for id in ids.split(',')]
            queryset = self.queryset.filter(sports_exercise__sport__id__in=sport_ids)
        if workzone_codes:
            workzone_codes = [str(id) for ids in workzone_codes for id in ids.split(',')]
            queryset = self.queryset.filter(zone_exercises__zone__code__in=workzone_codes)

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
    
    def latest(self, request):
        print('latest')
        latest_recipes = self.get_latest()
        serializer = self.serializer_class(latest_recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(serializer.data)
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

