from django.contrib.auth.models import Group, User
from rest_framework import serializers
from viewer.models import User, Sport, Material, Exercise, ExerciseStep, ExerciseMaterial, ExerciseSport, ExerciseZone, WorkZone, UsersFavExercises

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class ExerciseStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseStep
        fields = '__all__'

class ExerciseMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseMaterial
        fields = '__all__'

class ExerciseSportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseSport
        fields = '__all__'

class ExerciseZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseZone
        fields = '__all__'

class WorkZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkZone
        fields = '__all__'

class UsersFavExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersFavExercises
        fields = '__all__'