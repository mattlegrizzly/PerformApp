from rest_framework import serializers
from .models import Sport, Material, Exercise, ExerciseStep, ExerciseSport, ExerciseZone, WorkZone, ExerciseMaterial
from sport.serializers import SportSerializer

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'name', 'description', 'pictures']

#Creation serializer only with id
class ExerciseStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseStep
        fields = ['text', 'exercise']

#Detailed serializer for Exercise Serializer
class ExerciseStepDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseStep
        fields = ['text'] 

#Creation serializer only with id
class ExerciseMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseMaterial
        fields = ['material', 'exercise']

#Detailed serializer for Exercise Serializer
class ExerciseMaterialDetailedSerializer(serializers.ModelSerializer):
    material = MaterialSerializer(many=False)
    class Meta:
        model = ExerciseMaterial
        fields = ['material']

#Creation serializer only with id
class ExerciseSportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseSport
        fields = ['exercise', 'sport']

#Detailed serializer for Exercise Serializer
class ExerciseSportDetailedSerializer(serializers.ModelSerializer):
    sport = SportSerializer(many=False)
    class Meta:
        model = ExerciseSport
        fields = ['sport']

class WorkZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkZone
        fields = ['name', 'zone']

#Creation serializer only with id
class ExerciseZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseZone
        fields = ['zone', 'exercise']

#Detailed serializer for Exercise Serializer
class ExerciseZoneDetailedSerializer(serializers.ModelSerializer):
    zone=WorkZoneSerializer(many=False)
    class Meta:
        model = ExerciseZone
        fields = ['zone']


class ExerciseSerializer(serializers.ModelSerializer):
    steps_exercise = ExerciseStepDetailedSerializer(many=True, read_only=True)
    material_exercise = ExerciseMaterialDetailedSerializer(many=True, read_only=True)
    sports_exercise = ExerciseSportDetailedSerializer(many=True, read_only=True)
    zone_exercise = ExerciseZoneDetailedSerializer(many=True, read_only=True)
    class Meta:
        model = Exercise
        fields = ['name', 'description', 'video', 'steps_exercise', 'material_exercise', 'zone_exercise', 'sports_exercise']



