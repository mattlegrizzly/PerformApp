from django.db import models
from sport.models import Sport

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Zone(models.TextChoices):
    muscle = 'MU', "Muscle"
    articulation = 'AR', "Articulation"

class WorkZone(models.Model):
    name = models.CharField(max_length=100)
    zone = models.CharField(choices=Zone.choices , default=Zone.muscle, max_length=2)
    def getZone(self) -> Zone:
        # Get value from choices enum
        return self.zone(self.zone)

class Material(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    pictures = models.ImageField(upload_to=upload_to, blank=True, null=True)

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    video = models.CharField(max_length=255)

class ExerciseStep(models.Model):
    text = models.CharField(max_length=255)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="steps")

class ExerciseMaterial(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="materials")
    material = models.ForeignKey(Material, on_delete=models.CASCADE)

class ExerciseSport(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='sports')
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

class ExerciseZone(models.Model):
    zone = models.ForeignKey(WorkZone, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="zones")
