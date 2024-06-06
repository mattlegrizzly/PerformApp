from rest_framework import permissions, viewsets
from .models import Sport, SportsUser
from .serializers import SportSerializer, SportsUserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class SportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer

    @action(detail=False, methods=['get'], url_path="all")
    def all(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class SportsUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SportsUser.objects.all()
    serializer_class = SportsUserSerializer