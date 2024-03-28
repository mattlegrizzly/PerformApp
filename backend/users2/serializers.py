from rest_framework import serializers
from .models import User, UsersFavExercises, Injurie, Wellness
from sport.serializers import SportsUserSerializer
from exercise.serializers import ExerciseSerializer, WorkZoneSerializer

class UsersFavExercisesSerializer(serializers.ModelSerializer):
    exercices = ExerciseSerializer(many=True, read_only=False)
    class Meta:
        model = UsersFavExercises
        fields = ['exercices']

class InjurieSerializer(serializers.ModelSerializer):
    zone = WorkZoneSerializer(many=False, read_only=True)
    class Meta:
        model = Injurie
        fields = ['name', 'description', 'state', 'user', 'zone']

class WellnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wellness
        fields = ['sleep', 'hydratation', 'fatigue', 'pain', 'stress', 'date', 'user']

class UserSerializer(serializers.ModelSerializer):
    sports_user = SportsUserSerializer(many=True, read_only=False)
    user_injuries = InjurieSerializer(many=True, read_only=False)
    users_wellness = WellnessSerializer(many=True, read_only=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'size', 'age', 'gender', 'profile_picture', 'sports_user', 'user_injuries', 'users_wellness']


