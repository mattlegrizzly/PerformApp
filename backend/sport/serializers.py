from rest_framework import serializers
from .models import Sport, SportsUser
from users2.permissions import UserViewSetPermissions

class SportSerializer(serializers.ModelSerializer):
    permission_classes = [UserViewSetPermissions]
    class Meta:
        model = Sport
        fields = ['id', 'name']

class SportsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportsUser
        fields = ['user', 'sport']

class SportsDetailedUserSerializer(serializers.ModelSerializer):
    sport = SportSerializer()
    class Meta:
        model = SportsUser
        fields = ["id", 'sport']