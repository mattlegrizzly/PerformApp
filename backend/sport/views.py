from rest_framework import permissions, viewsets
from .models import Sport, SportsUser
from .serializers import SportSerializer, SportsUserSerializer, SportsDetailedUserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from users2.permissions import IsUserOrAdmin
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from rest_framework import filters, mixins, status, viewsets, pagination
from rest_framework.exceptions import ValidationError
# Create your views here.

class SportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer

    @action(detail=False, methods=['get'], url_path="all")
    def all(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class SportsUserViewSet(viewsets.ModelViewSet):
    queryset = SportsUser.objects.all()
    serializer_class = SportsUserSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsUserOrAdmin]
        return [permission() for permission in permission_classes]

    @extend_schema(
        tags=['Sports User'],
        responses={200: "OK"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(
        tags=['Sports User'],
        responses={200: "OK"}
    )
    @action(detail=False, methods=['get'], url_path="latest")
    def latest(self, request):
        latest_sports_user = self.get_latest()
        serializer = self.serializer_class(latest_sports_user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        tags=['Sports User'],
        responses={200: "OK"}
    )
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = SportsDetailedUserSerializer(instance)
        return Response(serializer.data)

    @extend_schema(
        tags=['Sports User'],
        responses={201: "Created"}
    )
    def create(self, request, *args, **kwargs):
        user_id = request.data.get('user')
        sport_id = request.data.get('sport')
        
        if self.queryset.filter(user=user_id, sport=sport_id).exists():
            raise ValidationError("An entry with this user and sport already exists.")

        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=['Sports User'],
        responses={200: "OK"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=['Sports User'],
        responses={200: "OK"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=['Sports User'],
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)