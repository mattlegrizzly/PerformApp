from rest_framework import serializers
from .models import User, UsersFavExercises, Injurie, Wellness
from sport.serializers import SportsUserSerializer
from exercise.serializers import ExerciseSerializer, WorkZoneSerializer
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken

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

    def check_email_exists(self, email, new_email):
        if User.objects.exclude(email=email).filter(email=new_email).exists():
            return True
        else:
            return False

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user



class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=255, allow_blank=False)

    class Meta:
        model = User
        fields = ["email", "password"]


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()


class RefreshTokensSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = RefreshToken(attrs["refresh"])

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        return data


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=255, allow_blank=False)

    class Meta:
        model = User
        fields = ["email", "password", "username", "gender", "age", "size"]

    def save(self):
        user = User(
            email=self.validated_data["email"],
            gender=self.validated_data["gender"],
            age=self.validated_data["age"],
            size=self.validated_data["size"],
            username=self.validated_data["username"],
        )
        password = self.validated_data["password"]
        user.set_password(password)
        user.save()

        return user


class SetPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=8, max_length=255, allow_blank=False, required=True
    )

    class Meta:
        model = User
        fields = ["password"]
