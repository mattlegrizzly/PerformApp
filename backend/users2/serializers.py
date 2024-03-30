from rest_framework import serializers
from .models import User, UsersFavExercises, Injurie, Wellness
from sport.serializers import SportsUserSerializer
from exercise.serializers import ExerciseSerializer, WorkZoneSerializer

class UsersFavExercisesSerializer(serializers.ModelSerializer):
    exercices = ExerciseSerializer(many=True, read_only=False)
    class Meta:
        model = UsersFavExercises
        fields = ['exercices']

class InjurieSerializer(serializers.ModelSerializer):
    zone = WorkZoneSerializer(many=False, read_only=True)
    class Meta:
        model = Injurie
        fields = ['name', 'description', 'state', 'user', 'zone']

class WellnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wellness
        fields = ['sleep', 'hydratation', 'fatigue', 'pain', 'stress', 'date', 'user']

class UserSerializer(serializers.ModelSerializer):
    sports_user = SportsUserSerializer(many=True, read_only=False)
    user_injuries = InjurieSerializer(many=True, read_only=False)
    users_wellness = WellnessSerializer(many=True, read_only=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'size', 'age', 'gender', 'profile_picture', 'sports_user', 'user_injuries', 'users_wellness']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        email = data.get('email')
        username = data.get('username')
        
        # Vérifier si l'utilisateur existe déjà avec l'email
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Cet email est déjà utilisé.")
        
        # Vérifier si l'utilisateur existe déjà avec le nom d'utilisateur
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("Ce nom d'utilisateur est déjà utilisé.")
        
        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    date_of_birth = serializers.DateField(required=False, allow_null=True)
    size = serializers.IntegerField(required=False, allow_null=True)
    age = serializers.IntegerField(required=False, allow_null=True)
    gender = serializers.ChoiceField(choices=User.GENDER_CHOICES)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Ce nom d'utilisateur est déjà utilisé.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Cet email est déjà utilisé.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
