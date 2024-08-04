from rest_framework import serializers
from .models import Workout
from users2.permissions import UserViewSetPermissions

class WorkoutSerializer(serializers.ModelSerializer):
    permission_classes = [UserViewSetPermissions]
    class Meta:
        model = Workout
        fields = ['id', 'name', 'date', 'workout_description', 'cognitive_rpe','physical_rpe','time_value', 'user']