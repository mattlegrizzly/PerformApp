from rest_framework import permissions, viewsets
from .models import User, UsersFavExercises, Wellness, Injurie
from .serializers import UserSerializer, UsersFavExercisesSerializer, InjurieSerializer, WellnessSerializer
from users2.permissions import UserViewSetPermissions


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [UserViewSetPermissions]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UsersFavExercisesViewSet(viewsets.ModelViewSet):
    permission_classes = [UserViewSetPermissions]
    queryset = UsersFavExercises.objects.all()
    serializer_class = UsersFavExercisesSerializer

class InjurieViewSet(viewsets.ModelViewSet):
    permission_classes = [UserViewSetPermissions]
    queryset = Injurie.objects.all()
    serializer_class = InjurieSerializer

class WellnessViewSet(viewsets.ModelViewSet):
    permission_classes = [UserViewSetPermissions]
    queryset = Wellness.objects.all()
    serializer_class = WellnessSerializer
