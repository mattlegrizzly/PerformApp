from django.db import models

# Create your models here.
class Workout(models.Model):
    name = models.CharField(max_length=100, unique=False, null=False)
    date = models.DateTimeField(auto_now_add=False, null=False)
    workout_description = models.TextField(blank=False, null=False)
    cognitive_rpe = models.BigIntegerField(blank=False, null=False)
    user = models.ForeignKey('users2.User', on_delete=models.CASCADE)
    physical_rpe = models.BigIntegerField(blank=False, null=False)
    time_value = models.DurationField(null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)