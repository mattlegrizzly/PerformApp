from django.db import models
from sport.models import Sport
from typing import List
from datetime import datetime

def upload_to_video(instance, filename):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    ext = filename.split('.')[-1]  # Récupérer l'extension du fichier
    filename_edit = f"exercice_{instance.id}_{timestamp}.{ext}"
    print(instance)
    return 'video/{filename}'.format(filename=filename_edit)

def upload_to(instance, filename):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    ext = filename.split('.')[-1]  # Récupérer l'extension du fichier
    filename_edit = f"material_{instance.id}_{timestamp}.{ext}"
    return 'images/{filename}'.format(filename=filename_edit)

class Zone(models.TextChoices):
    muscle = 'MU', "Muscle"
    articulation = 'AR', "Articulation"

class WorkZone(models.Model):
    name = models.CharField(max_length=100, null=False)
    code = models.CharField(max_length=100, null=False, primary_key=True)
    zone = models.CharField(choices=Zone.choices , default=Zone.muscle, max_length=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    def getZone(self) -> Zone:
        # Get value from choices enum
        return self.zone(self.zone)

class Material(models.Model):
    name = models.CharField(max_length=100)
    pictures = models.ImageField(upload_to=upload_to, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    video = models.FileField(upload_to=upload_to_video, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    materials = models.ManyToManyField(to=Material, through="exercise.ExerciseMaterial")
    sports = models.ManyToManyField(to=Sport, through="exercise.ExerciseSport")

    @property
    def material_ids(self) -> List[int]:
        return [material.id for material in self.materials.all()]
    
    @property
    def sports_ids(self) -> List[int]:
        return [sport.id for sport in self.sports.all()]

class ExerciseStep(models.Model):
    text = models.CharField(max_length=255)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="steps_exercise")

class ExerciseMaterial(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="material_exercise")

class ExerciseSport(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='sports_exercise')

class ExerciseZone(models.Model):
    zone = models.ForeignKey(WorkZone, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="zone_exercises")
