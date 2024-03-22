from rest_framework import serializers
from .models import Sport, SportsUser

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ['name']

class SportsUserSerializer(serializers.ModelSerializer):
    sport = SportSerializer()
    class Meta:
        model = SportsUser
        fields = ['sport']