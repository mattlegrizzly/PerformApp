from rest_framework import viewsets
from .models import Material, Exercise, ExerciseStep, ExerciseMaterial, ExerciseSport, ExerciseZone, WorkZone
from .serializers import MaterialSerializer, ExerciseSerializer, ExerciseStepSerializer, ExerciseMaterialSerializer, ExerciseSportSerializer, ExerciseZoneSerializer, WorkZoneSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from rest_framework.response import Response
from rest_framework import filters, mixins, status, viewsets, pagination
from rest_framework.decorators import action
from utils.utils import get_ordered_queryset
from django.db.models import Count, Q
#------------------MATERIAL------------------
# List/Get ViewSet
class MaterialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    
    @action(detail=False, methods=['get'], url_path="all")
    def all(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

#------------------EXERCISE------------------
# List/Get ViewSet
class ExerciseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "materials__name", "sports__name"]

    @action(detail=False, methods=['get'], url_path="all")
    def all(self, request):
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
        # Filtrer le queryset
        queryset = self.filter_queryset(queryset)

        # Sinon, sérialiser le queryset complet
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def get_queryset(self):
        queryset = Exercise.objects.all()
        return queryset

    def get_latest(self):
        queryset = Exercise.objects.all().order_by("created_at")[:5]
        return queryset

    def list(self, request, *args, **kwargs):
        # Appliquer l'ordre initial par id si nécessaire
        queryset = get_ordered_queryset(self.queryset, request.query_params)

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

        queryset = queryset.distinct()
        
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
    
    @action(detail=False, methods=['get'], url_path="all")
    def all(self, request):
        queryset = self.get_queryset()
        # Exclure les muscles contenant "droit" ou "gauche" dans le nom
        queryset = queryset.exclude(Q(name__icontains="droit") | Q(name__icontains="gauche"))
        queryset = queryset.order_by("name")
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path="all_injury")
    def all_injury(self, request):
    # Trouver les codes des muscles ayant des versions "left" et "right"
        main_codes_with_sides = (
            self.get_queryset()
            .filter(Q(code__icontains="-left") | Q(code__icontains="-right"))
            .values_list('code', flat=True)
            .distinct()
        )
        
        # Extraire les codes principaux (sans "-left" ni "-right")
        main_codes = set(code.rsplit('-', 1)[0] for code in main_codes_with_sides)
        
        # Muscles ayant des versions "left" et "right"
        left_right_muscles = self.get_queryset().filter(
            Q(code__icontains="-left") | Q(code__icontains="-right")
        )
        
        # Muscles n'ayant pas de versions "left" et "right"
        single_muscles = self.get_queryset().exclude(
            Q(code__icontains="-left") | Q(code__icontains="-right") | Q(code__in=main_codes)
        )

        # Combiner les deux ensembles de muscles
        queryset = left_right_muscles | single_muscles
        queryset = queryset.order_by("name")

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
