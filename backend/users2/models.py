from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email, MinLengthValidator, EmailValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from exercise.models import Exercise, WorkZone

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Manager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have a password")

        email = self.normalize_email(email)
        validate_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, first_name, last_name, email, password):
        user = self.create_user(
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_coach = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]
    email = models.EmailField(_('email address'), unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    size = models.IntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to=upload_to, blank=True, null=True)
    is_superuser = models.BooleanField(default=False, blank=False, null=False)
    is_active = models.BooleanField(default=True, blank=False, null=False)
    is_coach = models.BooleanField(default=False, blank=False, null=False)
    is_staff = models.BooleanField(default=False, blank=False, null=False)
    last_login = models.DateTimeField(default=None, null=True, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    
    objects = Manager()
    
    def __repr__(self):
        return str(self)

    def get_obj(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "is_superuser": self.is_superuser,
            "is_active": self.is_active,
            "last_login": self.last_login,
        }

    def get_str(self):
        return (
            f"User(id={self.id}, email={self.email},"
            f"first_name={self.first_name}, last_name={self.last_name}, "
            f"is_superuser={self.is_superuser}, is_active={self.is_active}, last_login={self.last_login})"
        )

class State(models.TextChoices):
    TREATED = 'TR', "Soignée"
    not_treated = 'NT', "Pas soignée"
    in_progress = 'IP', "En cours"


class UsersFavExercises(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fav_exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

class Injurie(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=256, default="Rien à signaler")
    state = models.CharField(choices=State.choices , default=State.not_treated, max_length=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_injuries")
    zone = models.ForeignKey(WorkZone, on_delete=models.CASCADE)

class Wellness(models.Model):
    hydratation = models.IntegerField(null=False, default=0, blank=True)
    sleep = models.IntegerField(null=False, default=0, blank=True)
    stress = models.IntegerField(null=False, default=0, blank=True)
    fatigue = models.IntegerField(null=False, default=0, blank=True)
    pain = models.IntegerField(null=False, default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_wellness')
    date = models.DateField(null=False)