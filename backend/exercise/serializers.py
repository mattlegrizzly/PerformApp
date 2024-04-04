from rest_framework import serializers
from .models import Sport, Material, Exercise, ExerciseStep, ExerciseSport, ExerciseZone, WorkZone, ExerciseMaterial
from sport.serializers import SportSerializer

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'name', 'description', 'pictures']

class ExerciseStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseStep
        fields = ['id', 'text', 'exercise']

class ExerciseMaterialSerializer(serializers.ModelSerializer):
    material = MaterialSerializer(many=False, read_only=False)
    class Meta:
        model = ExerciseMaterial
        fields = ['exercise', 'material']

class ExerciseSportSerializer(serializers.ModelSerializer):
    sport = SportSerializer(many=False, read_only=False)
    class Meta:
        model = ExerciseSport
        fields = ['exercise', 'sport']

class WorkZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkZone
        fields = ['name', 'zone']

class ExerciseZoneSerializer(serializers.ModelSerializer):
    zone=WorkZoneSerializer(many=False)
    class Meta:
        model = ExerciseZone
        fields = '__all__'


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['name', 'description', 'video']



