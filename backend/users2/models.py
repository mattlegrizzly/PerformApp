from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from exercise.models import Exercise, WorkZone

from .managers import CustomUserManager

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class User(AbstractUser):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]
    email = models.EmailField(_('email address'), unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    size = models.IntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to=upload_to, blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']




class State(models.TextChoices):
    TREATED = 'TR', "Soignée"
    not_treated = 'NT', "Pas soignée"
    in_progress = 'IP', "En cours"


class UsersFavExercises(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fav_exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

class Injurie(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=256)
    state = models.CharField(choices=State.choices , default=State.not_treated, max_length=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    zone = models.ForeignKey(WorkZone, on_delete=models.CASCADE)