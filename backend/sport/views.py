from rest_framework import permissions, viewsets
from .models import Sport, SportsUser
from .serializers import SportSerializer, SportsUserSerializer

# Create your views here.

class SportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer

class SportsUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SportsUser.objects.all()
    serializer_class = SportsUserSerializer