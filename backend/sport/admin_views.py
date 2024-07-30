from rest_framework import permissions, viewsets
from .models import Sport, SportsUser
from .serializers import SportSerializer, SportsUserSerializer, SportsDetailedUserSerializer, RecordsSport, RecordsSportDetailedUserSerializer, RecordsSportSerializer, RecordsSportUser, RecordsSportUserSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from rest_framework import filters, mixins, status, viewsets, pagination
from rest_framework.decorators import action
from rest_framework.response import Response
from utils.utils import get_ordered_queryset

#------------------SPORT------------------
# Admin ViewSet
class AdminSportViewSet(viewsets.ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
    @extend_schema(
        tags=['Admin - Sport'],
        responses={200: "OK"}
    )
    @action(detail=False, methods=['get'], url_path="all")
    def get(self, request):
        # Récupérez toutes les entités de votre modèle sans limite
        items = Sport.objects.all()        
        items = get_ordered_queryset(self.queryset, self.request.query_params)
        # Sérialisez les données
        serializer = SportSerializer(items, many=True)
        # Retournez la réponse
        return Response(serializer.data)
    
    @extend_schema(
        tags=['Admin - Sport'],
        responses={200: "OK"}
    )
    def get_queryset(self):
        queryset = Sport.objects.all()
        return queryset

    @extend_schema(
        tags=['Admin - Sport'],
        responses={200: "OK"}
    )
    def get_latest(self):
        queryset = Sport.objects.all().order_by("created_at")[:5]
        return queryset

    @extend_schema(
        tags=['Admin - Sport'],
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
        tags=['Admin - Sport'],
        responses={200: "OK"}
    )
    @action(detail=False, methods=['get'], url_path="latest")
    def latest(self, request):
        latest_sports = self.get_latest()
        serializer = self.serializer_class(latest_sports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(
        tags=['Admin - Sport'],
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Sport'],
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Sport'],
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Sport'],
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Sport'],
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

#------------------SPORT_USER------------------
# Admin ViewSet
class AdminSportsUserViewSet(viewsets.ModelViewSet):
    queryset = SportsUser.objects.all()
    serializer_class = SportsUserSerializer
    permission_classes = [permissions.IsAdminUser]

    @extend_schema(
        tags=['Admin - Sports User'],
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(
        tags=['Admin - Sports User'],
        responses={200: "OK"}
    )
    @action(detail=False, methods=['get'], url_path="latest")
    def latest(self, request):
        latest_sports_user = self.get_latest()
        serializer = self.serializer_class(latest_sports_user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        tags=['Admin - Sports User'],
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = SportsDetailedUserSerializer(instance)
        return Response(serializer.data)

    @extend_schema(
        tags=['Admin - Sports User'],
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Sports User'],
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Sports User'],
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Sports User'],
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
#------------------ADMIN_RECORDS_SPORTS------------------
# Admin ViewSet
class AdminRecordsSportViewSet(viewsets.ModelViewSet):
    queryset = RecordsSport.objects.all()
    serializer_class = RecordsSportSerializer
    permission_classes = [permissions.IsAdminUser]

    @extend_schema(
        tags=['Admin - Records Sport'],
        responses={200: RecordsSportSerializer(many=True)}
    )
    @action(detail=False, methods=['get'], url_path="all")
    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @extend_schema(
        tags=['Admin - Records Sport'],
        responses={200: RecordsSportSerializer}
    )
    def get_queryset(self):
        queryset = RecordsSport.objects.all()
        return queryset

    @extend_schema(
        tags=['Admin - Records Sport'],
        responses={200: RecordsSportSerializer(many=True)}
    )
    def get_latest(self):
        queryset = RecordsSport.objects.all().order_by("created_at")[:5]
        return queryset

    @extend_schema(
        tags=['Admin - Records Sport'],
        responses={200: RecordsSportSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

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
        tags=['Admin - Records Sport'],
        responses={200: RecordsSportSerializer(many=True)}
    )
    @action(detail=False, methods=['get'], url_path="latest")
    def latest(self, request):
        latest_records_sport = self.get_latest()
        serializer = self.serializer_class(latest_records_sport, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        tags=['Admin - Records Sport'],
        responses={200: RecordsSportSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Records Sport'],
        responses={201: RecordsSportSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Records Sport'],
        responses={200: RecordsSportSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Records Sport'],
        responses={200: RecordsSportSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Records Sport'],
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    @extend_schema(
        tags=['Admin - Records Sport'],
        responses={200: RecordsSportSerializer(many=True)}
    )
    @action(detail=False, methods=['get'], url_path="by-sport")
    def by_sport(self, request):
        sport_id = request.query_params.get('sport_id')
        if not sport_id:
            return Response({"detail": "sport_id query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = self.get_queryset().filter(sport_id=sport_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#------------------ADMIN_USER_RECORDS_SPORTS------------------
# Admin ViewSet
class AdminRecordsSportUserViewSet(viewsets.ModelViewSet):
    queryset = RecordsSportUser.objects.all()
    serializer_class = RecordsSportUserSerializer
    permission_classes = [permissions.IsAdminUser]

    @extend_schema(
        tags=['Admin - Records Sport User'],
        responses={200: RecordsSportUserSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(
        tags=['Admin - Records Sport User'],
        responses={200: RecordsSportUserSerializer(many=True)}
    )
    @action(detail=False, methods=['get'], url_path="latest")
    def latest(self, request):
        latest_records_user = self.get_queryset().order_by('-created_at')[:5]  # Example logic for latest
        serializer = self.get_serializer(latest_records_user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        tags=['Admin - Records Sport User'],
        responses={200: RecordsSportDetailedUserSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = RecordsSportDetailedUserSerializer(instance)
        return Response(serializer.data)

    @extend_schema(
        tags=['Admin - Records Sport User'],
        responses={201: RecordsSportUserSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Records Sport User'],
        responses={200: RecordsSportUserSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Records Sport User'],
        responses={200: RecordsSportUserSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Admin - Records Sport User'],
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)