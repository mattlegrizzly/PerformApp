from rest_framework import serializers
from .models import Sport, SportsUser, RecordsSport, RecordsSportUser, RecordsGroupSport
from users2.permissions import UserViewSetPermissions

class SportSerializer(serializers.ModelSerializer):
    permission_classes = [UserViewSetPermissions]
    class Meta:
        model = Sport
        fields = ['id', 'name', 'isTheme']

class SportSerializer(serializers.ModelSerializer):
    permission_classes = [UserViewSetPermissions]
    class Meta:
        model = Sport
        fields = ['id', 'name', 'isTheme']

class SportsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportsUser
        fields = ['user', 'sport',]

class SportsDetailedUserSerializer(serializers.ModelSerializer):
    sport = SportSerializer()
    class Meta:
        model = SportsUser
        fields = ["id", 'sport']

class RecordsGroupSportSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordsGroupSport
        fields = ['id', 'name', 'sport', 'is_general']

class RecordsSportSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordsSport
        fields = ['id', 'sport', 'units', 'order', 'name', 'groups', 'general']

class RecordsSportUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordsSportUser
        fields = ['id', 'record', 'user', 'time_value', 'record_value', 'free_value', 'created_at', 'updated_at', 'date_record']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.record.units == 'time':
            representation.pop('record_value')
        elif instance.record.units == 'weight' or instance.record.units == 'points' or instance.record.units == 'distance_m' or instance.record.units == 'distance_km':
            representation.pop('time_value')
        elif instance.record.units == 'free':
            representation.pop('time_value')
            representation.pop('record_value')
        return representation

class RecordsSportDetailedUserSerializer(serializers.ModelSerializer):
    record = RecordsSportSerializer()
    user = serializers.StringRelatedField()  # Affiche le nom d'utilisateur au lieu de l'ID

    class Meta:
        model = RecordsSportUser
        fields = ['id', 'record', 'user', 'time_value', 'free_value','record_value', 'created_at', 'updated_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.record.units == 'time':
            representation.pop('record_value')
        elif instance.record.units == 'weight' or instance.record.units == 'points' or instance.record.units == 'distance_m' or instance.record.units == 'distance_km':
            representation.pop('time_value')
        elif instance.record.units == 'free':
            representation.pop('time_value')
            representation.pop('record_value')
        return representation