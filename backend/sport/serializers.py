from rest_framework import serializers
from .models import Sport, SportsUser, RecordsSport, RecordsSportUser
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

class RecordsSportSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordsSport
        fields = ['id', 'sport', 'units', 'name']

class RecordsSportUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordsSportUser
        fields = ['record', 'user', 'time_value', 'weight_value', 'created_at', 'updated_at', 'date_record']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.record.units == 'time':
            representation.pop('weight_value')
        elif instance.record.units == 'weight':
            representation.pop('time_value')
        return representation

class RecordsSportDetailedUserSerializer(serializers.ModelSerializer):
    record = RecordsSportSerializer()
    user = serializers.StringRelatedField()  # Affiche le nom d'utilisateur au lieu de l'ID

    class Meta:
        model = RecordsSportUser
        fields = ['id', 'record', 'user', 'time_value', 'weight_value', 'created_at', 'updated_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.record.units == 'time':
            representation.pop('weight_value')
        elif instance.record.units == 'weight':
            representation.pop('time_value')
        return representation