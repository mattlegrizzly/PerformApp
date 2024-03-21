from django.db import models
from users2.models import User

class Sport(models.Model):
    name = models.CharField(max_length=100)

class SportsUser(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Material(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    pictures = models.CharField(max_length=255)

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    video = models.CharField(max_length=255)

class ExerciseStep(models.Model):
    text = models.CharField(max_length=255)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

class ExerciseMaterial(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)

class ExerciseSport(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

class ExerciseZone(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    zone = models.ForeignKey('WorkZone', on_delete=models.CASCADE)

class WorkZone(models.Model):
    name = models.CharField(max_length=100)
    zone = models.CharField(max_length=100)

class UsersFavExercises(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fav_exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
