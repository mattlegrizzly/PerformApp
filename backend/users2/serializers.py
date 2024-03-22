from rest_framework import serializers
from .models import User, UsersFavExercises
from sport.serializers import SportsUserSerializer
from exercise.serializers import ExerciseSerializer

class UserSerializer(serializers.ModelSerializer):
    sports_user = SportsUserSerializer(many=True, read_only=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'size', 'age', 'gender', 'profile_picture', 'sports_user']


class UsersFavExercisesSerializer(serializers.ModelSerializer):
    exercices = ExerciseSerializer(many=True, read_only=False)
    class Meta:
        model = UsersFavExercises
        fields = ['exercices']