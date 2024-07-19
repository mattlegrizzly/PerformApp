from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework import filters, mixins, status, viewsets, pagination
from rest_framework.response import Response
import os
from sport.models import Sport
from .models import Material, Exercise, ExerciseStep, ExerciseMaterial, ExerciseSport, ExerciseZone, WorkZone
from .serializers import MaterialSerializer, ExerciseSerializer, ExerciseStepSerializer, ExerciseMaterialSerializer, ExerciseSportSerializer, ExerciseZoneSerializer, WorkZoneSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample

from utils.utils import get_ordered_queryset

#------------------MATERIAL------------------
# Admin ViewSet
class AdminMaterialViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
    @extend_schema(
        tags=['Admin - Material'],
        responses={200: "OK"}
    )
    @action(detail=False, methods=['get'], url_path="all")
    def get(self, request):
        items = Material.objects.all()
        
        items = get_ordered_queryset(self.queryset, request.query_params)
        # Récupérez toutes les entités de votre modèle sans limite
        # Sérialisez les données
        serializer = MaterialSerializer(items, many=True)
        # Retournez la réponse
        return Response(serializer.data)

    @extend_schema(
        tags=['Admin - Material'],
        responses={200: "OK"}
    )
    @action(detail=False, methods=['get'], url_path="all")
    def get_queryset(self):
        queryset = Material.objects.all()
        return queryset

    @extend_schema(
        tags=['Admin - Material'],
        responses={200: "OK"}
    )
    def get_latest(self):
        queryset = Material.objects.all().order_by("created_at")[:5]
        return queryset

    @extend_schema(
        tags=['Admin - Material'],
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        # Appliquer l'ordre initial par id si nécessaire
        queryset = get_ordered_queryset(self.queryset, request.query_params)

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
        tags=['Admin - Material'],
        responses={200: "OK"}
    )
    @action(detail=False, methods=['get'], url_path="latest")
    def latest(self, request):
        latest_materials = self.get_latest()
        serializer = self.serializer_class(latest_materials, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(
        tags=['Admin - Material'],
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Material'],
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_update(self, serializer):
        instance = serializer.instance
        old_photo_path = instance.pictures.path if instance.pictures else None
        if(old_photo_path):
            old_photo_name = old_photo_path.split('/')[-1]
            new_photo_path = serializer.validated_data.get('pictures')
            if old_photo_name and new_photo_path and old_photo_name != new_photo_path._name:
                # Supprimer le fichier vidéo précédent
                if os.path.isfile(old_photo_path):
                    os.remove(old_photo_path) 

        super().perform_update(serializer)  # Appel de la méthode perform_update de la classe parent

    @extend_schema(
        tags=['Admin - Material'],
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Material'],
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Material'],
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

#------------------EXERCISE------------------
# Admin ViewSet
class AdminExerciseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "materials__name", "sports__name"]

    @extend_schema(
        tags=['Admin - Exercise'],
        responses={200: "OK"}
    )
    def get_queryset(self):
        queryset = Exercise.objects.all()
        return queryset

    @extend_schema(
        tags=['Admin - Exercise'],
        responses={200: "OK"}
    )
    def get_latest(self):
        queryset = Exercise.objects.all().order_by("created_at")[:5]
        return queryset

    @extend_schema( 
        tags=['Admin - Exercise'],
        responses={200: "OK"}
    )
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
        tags=['Admin - Exercise'],
        responses={200: "OK"}
    )
    @action(detail=False, methods=['get'], url_path="latest")
    def latest(self, request):
        latest_exercises = self.get_latest()
        search_term = self.request.query_params.get("search")
        if search_term:
            queryset = queryset.filter(name=search_term)
        serializer = self.serializer_class(latest_exercises, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(
        tags=['Admin - Exercise'],
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    @extend_schema(
        tags=['Admin - Exercise'],
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        instance = serializer.instance
        old_video_path = instance.video.path if instance.video else None
        if(old_video_path): 
            old_video_name = old_video_path.split('/')[-1]
            new_video_path = serializer.validated_data.get('video')
            if old_video_name and new_video_path and old_video_name != new_video_path._name:
                # Supprimer le fichier vidéo précédent
                if os.path.isfile(old_video_path):
                    os.remove(old_video_path) 

        super().perform_update(serializer)  # Appel de la méthode perform_update de la classe parent

    @extend_schema(
        tags=['Admin - Exercise'],
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        data = request.data
        def update_relationships(obj, field_name, model, data_key, lookup_field='id'):
            ids = data.get(data_key, [])
            if ids != "" and isinstance(ids, str):
                ids = [int(num) for num in ids.split(",")]
            if list(getattr(obj, field_name).values_list(lookup_field, flat=True)) != ids:
                new_items = model.objects.filter(**{f"{lookup_field}__in": ids})
                getattr(obj, field_name).set(new_items)
                obj.save()

        obj = self.get_object()
        update_relationships(obj, "materials", Material, "material_ids")
        update_relationships(obj, "sports", Sport, "sports_ids")
        update_relationships(obj, "muscles", WorkZone, "muscles_id", lookup_field='code')
        
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise'],
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise'],
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

#------------------EXERCISE_STEPS------------------
# Admin ViewSet
class AdminExerciseStepViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = ExerciseStep.objects.all()
    serializer_class = ExerciseStepSerializer

    @extend_schema(
        tags=['Admin - Exercise Step'],
        responses={200: "OK"}
    )
    def get_queryset(self):
        queryset = ExerciseStep.objects.all()
        return queryset

    @extend_schema(
        tags=['Admin - Exercise Step'],
        responses={200: "OK"}
    )
    def get_latest(self):
        queryset = ExerciseStep.objects.all().order_by("created_at")[:5]
        return queryset

    @extend_schema(
        tags=['Admin - Exercise Step'],
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        # Appliquer l'ordre initial par id si nécessaire
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
        tags=['Admin - Exercise Step'],
        responses={200: "OK"}
    )
    @action(detail=False, methods=['get'], url_path="latest")
    def latest(self, request):
        latest_exercise_step = self.get_latest()
        serializer = self.serializer_class(latest_exercise_step, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        tags=['Admin - Exercise Step'],
        responses={200: "OK"}
    )
    @action(detail=False, methods=['get'], url_path="exercise/(?P<exercise_id>\d+)")
    def exercise(self, request, *args, **kwargs):
        exercise_id = kwargs.get('exercise_id')
        queryset = self.queryset.filter(exercise=exercise_id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        tags=['Admin - Exercise Step'],
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Step'],
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Step'],
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Step'],
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Step'],
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({}, status=status.HTTP_204_NO_CONTENT)

#------------------EXERCISE_MATERIAL------------------
# Admin ViewSet
class AdminExerciseMaterialViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = ExerciseMaterial.objects.all()
    serializer_class = ExerciseMaterialSerializer

    @extend_schema(
        tags=['Admin - Exercise Material'],
        responses={200: "OK"}
    )
    def get_queryset(self):
        queryset = ExerciseMaterial.objects.all()
        return queryset

    @extend_schema(
        tags=['Admin - Exercise Material'],
        responses={200: "OK"}
    )
    def get_latest(self):
        queryset = ExerciseMaterial.objects.all().order_by("created_at")[:5]
        return queryset

    @extend_schema(
        tags=['Admin - Exercise Material'],
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        # Appliquer l'ordre initial par id si nécessaire
        queryset = get_ordered_queryset(self.queryset, request.query_params)

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
        tags=['Admin - Exercise Material'],
        responses={200: "OK"}
    )
    @action(detail=False, methods=['get'], url_path="latest")
    def latest(self, request):
        latest_exercise_material = self.get_latest()
        serializer = self.serializer_class(latest_exercise_material, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        tags=['Admin - Exercise Material'],
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Material'],
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Material'],
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Material'],
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Material'],
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

#------------------EXERCISE_SPORTS------------------
# Admin ViewSet
class AdminExerciseSportViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = ExerciseSport.objects.all()
    serializer_class = ExerciseSportSerializer

    @extend_schema(
        tags=['Admin - Exercise Sport'],
        responses={200: "OK"}
    )
    def get_queryset(self):
        queryset = ExerciseSport.objects.all()
        return queryset

    @extend_schema(
        tags=['Admin - Exercise Sport'],
        responses={200: "OK"}
    )
    def get_latest(self):
        queryset = ExerciseSport.objects.all().order_by("created_at")[:5]
        return queryset

    @extend_schema(
        tags=['Admin - Exercise Sport'],
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        # Appliquer l'ordre initial par id si nécessaire
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
        tags=['Admin - Exercise Sport'],
        responses={200: "OK"}
    )
    @action(detail=False, methods=['get'], url_path="latest")
    def latest(self, request):
        latest_exercise_sport = self.get_latest()
        serializer = self.serializer_class(latest_exercise_sport, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(
        tags=['Admin - Exercise Sport'],
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Sport'],
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Sport'],
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Sport'],
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Sport'],
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

#------------------EXERCISE_Zone------------------
# Admin ViewSet
class AdminExerciseZoneViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = ExerciseZone.objects.all()
    serializer_class = ExerciseZoneSerializer

    @extend_schema(
        tags=['Admin - Exercise Zone'],
        responses={200: "OK"}
    )
    def get_queryset(self):
        queryset = ExerciseZone.objects.all()
        return queryset

    @extend_schema(
        tags=['Admin - Exercise Zone'],
        responses={200: "OK"}
    )
    def get_latest(self):
        queryset = ExerciseZone.objects.all().order_by("created_at")[:5]
        return queryset

    @extend_schema(
        tags=['Admin - Exercise Zone'],
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        if request.query_params.get("itemsPerPage"):
            self.pagination_class.page_size = request.query_params.get("itemsPerPage")
        return super().list(request, *args, **kwargs)
    
    @extend_schema(
        tags=['Admin - Exercise Zone'],
        responses={200: "OK"}
    )
    @action(detail=False, methods=['get'], url_path="latest")
    def latest(self, request):
        latest_exercises_zone = self.get_latest()
        serializer = self.serializer_class(latest_exercises_zone, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(
        tags=['Admin - Exercise Zone'],
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Zone'],
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Zone'],
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Zone'],
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Exercise Zone'],
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

#------------------WORKZONE------------------
# Admin ViewSet
class AdminWorkZoneViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = WorkZone.objects.all()
    serializer_class = WorkZoneSerializer

    @extend_schema(
        tags=['Admin - Work Zone'],
        responses={200: "OK"}
    )
    @action(detail=False, methods=['get'], url_path="all")
    def get(self, request):
        # Récupérez toutes les entités de votre modèle sans limite
        items = WorkZone.objects.all()        
        items = self.queryset.order_by("name")

        # Sérialisez les données
        serializer = WorkZoneSerializer(items, many=True)
        # Retournez la réponse
        return Response(serializer.data)
    
    @extend_schema(
        tags=['Admin - Work Zone'],
        responses={200: "OK"}
    )
    def get_queryset(self):
        queryset = WorkZone.objects.all()
        return queryset

    @extend_schema(
        tags=['Admin - Work Zone'],
        responses={200: "OK"}
    )
    def get_latest(self):
        queryset = WorkZone.objects.all().order_by("created_at")[:5]
        return queryset

    @extend_schema(
        tags=['Admin - Work Zone'],
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        if request.query_params.get("itemsPerPage"):
            self.pagination_class.page_size = request.query_params.get("itemsPerPage")
        return super().list(request, *args, **kwargs)
    
    @extend_schema(
        tags=['Admin - Work Zone'],
        responses={200: "OK"}
    )
    @action(detail=False, methods=['get'], url_path="latest")
    def latest(self, request):
        latest_workzone = self.get_latest()
        serializer = self.serializer_class(latest_workzone, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    @extend_schema(
            tags=['Admin - Work Zone'],
            responses={200: "OK"}
        )
    def retrieve(self, request, *args, **kwargs):
        kwargs['lookup_field'] = 'code'
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Work Zone'],
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        kwargs['lookup_field'] = 'code'
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Work Zone'],
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        kwargs['lookup_field'] = 'code'
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Work Zone'],
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        kwargs['lookup_field'] = 'code'
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Work Zone'],
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        kwargs['lookup_field'] = 'code'
        return super().destroy(request, *args, **kwargs)