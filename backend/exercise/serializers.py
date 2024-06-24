from rest_framework import serializers
from .models import Sport, Material, Exercise, ExerciseStep, ExerciseSport, ExerciseZone, WorkZone, ExerciseMaterial
from sport.serializers import SportSerializer

class MaterialSerializer(serializers.ModelSerializer):
    pictures = serializers.ImageField(required=False)
    class Meta:
        model = Material
        fields = ['id', 'name', 'pictures']

#Creation serializer only with id
class ExerciseStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseStep
        fields = ['id', 'text', 'exercise']

#Detailed serializer for Exercise Serializer
class ExerciseStepDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseStep
        fields = ['id', 'text'] 

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
        fields = ['name', 'code', 'zone']

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
    steps_exercise = serializers.SerializerMethodField()
    material_exercise = ExerciseMaterialDetailedSerializer(many=True, read_only=True)
    sports_exercise = ExerciseSportDetailedSerializer(many=True, read_only=True)
    zone_exercises = ExerciseZoneDetailedSerializer(many=True, read_only=True)
    
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'video', 'thumbnail', 'steps_exercise', 'material_exercise', 'zone_exercises', 'sports_exercise', 'created_at']
    
    def get_steps_exercise(self, obj):
        steps = obj.steps_exercise.order_by('id')
        return ExerciseStepDetailedSerializer(steps, many=True, read_only=True).data



