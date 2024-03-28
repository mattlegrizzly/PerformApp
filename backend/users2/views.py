from rest_framework import permissions, viewsets
from .models import User, UsersFavExercises, Wellness, Injurie
from .serializers import UserSerializer, UsersFavExercisesSerializer, InjurieSerializer, WellnessSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UsersFavExercisesViewSet(viewsets.ModelViewSet):
    queryset = UsersFavExercises.objects.all()
    serializer_class = UsersFavExercisesSerializer

class InjurieViewSet(viewsets.ModelViewSet):
    queryset = Injurie.objects.all()
    serializer_class = InjurieSerializer

class WellnessViewSet(viewsets.ModelViewSet):
    queryset = Wellness.objects.all()
    serializer_class = WellnessSerializer
