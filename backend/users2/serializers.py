from rest_framework import serializers
from .models import User, UsersFavExercises, Injurie, Wellness
from sport.serializers import SportsDetailedUserSerializer
from exercise.serializers import ExerciseSerializer, WorkZoneSerializer
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class UsersFavExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersFavExercises
        fields = ['user', 'fav_exercise']

class UsersFavDetailedExercisesSerializer(serializers.ModelSerializer):
    fav_exercise = ExerciseSerializer(many=False, read_only=False)
    class Meta:
        model = UsersFavExercises
        fields = ["id",  'user', 'fav_exercise']

class InjurieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Injurie
        fields = ['name', 'description', 'state', 'user', 'zone', 'date']


class InjurieDetailedSerializer(serializers.ModelSerializer):
    zone = WorkZoneSerializer(many=False, read_only=False)
    class Meta:
        model = Injurie
        fields = ["id", 'name', 'description', 'state', 'user', 'zone', 'date']

class WellnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wellness
        fields = ['sleep', 'hydratation', 'fatigue', 'pain', 'stress', 'date', 'user']

class UserDetailedSerializer(serializers.ModelSerializer):
    sports_user = SportsDetailedUserSerializer(many=True, read_only=False)
    user_injuries = InjurieDetailedSerializer(many=True, read_only=False)
    users_wellness = WellnessSerializer(many=True, read_only=False)
    class Meta:
        model = User
        fields = [ 'id', 'email', 'first_name', 'last_name' , 'size', 'age', 'gender', 'profile_picture', 'sports_user', 'user_injuries', 'users_wellness', 'is_superuser']

    def check_email_exists(self, email, new_email):
        if User.objects.exclude(email=email).filter(email=new_email).exists():
            return True
        else:
            return False

class UserSerializer(serializers.ModelSerializer):
    sports_user = SportsDetailedUserSerializer(many=True, read_only=False)
    user_injuries = InjurieDetailedSerializer(many=True, read_only=False)
    users_wellness = WellnessSerializer(many=True, read_only=False)
    class Meta:
        model = User
        fields = [ 'id', 'email', 'first_name', 'last_name' , 'size', 'age', 'gender', 'profile_picture', 'sports_user', 'user_injuries', 'users_wellness', 'is_superuser']
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
        fields = ["email", "password","last_name", "first_name", "profile_picture", "gender", "age", "size"]

    def save(self):
        user = User(
            email=self.validated_data["email"],
            gender=self.validated_data["gender"],
            age=self.validated_data["age"],
            size=self.validated_data["size"],
            last_name=self.validated_data["last_name"],
            first_name=self.validated_data["first_name"],
            profile_picture=self.validated_data.get("profile_picture", None),
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
