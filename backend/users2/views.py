from rest_framework import permissions, viewsets
from .models import User, UsersFavExercises
from .serializers import UserSerializer, UsersFavExercisesSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UsersFavExercisesViewSet(viewsets.ModelViewSet):
    queryset = UsersFavExercises.objects.all()
    serializer_class = UsersFavExercisesSerializer