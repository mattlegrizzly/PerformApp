from django.db import models


class Sport(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class SportsUser(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    user = models.ForeignKey('users2.User', on_delete=models.CASCADE, related_name="sports_user")

class RecordsSport(models.Model):
    UNITS_CHOICE = [
        ('weight', 'Kilogrammes'),
        ('time', 'Temps')
    ]
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    units = models.CharField(max_length=10, choices=UNITS_CHOICE)
    name = models.CharField(max_length=100, unique=True, null=False)

class RecordsSportUser(models.Model):
    UNITS_CHOICE = [
        ('weight', 'Kilogrammes'),
        ('time', 'Temps')
    ]
    record = models.ForeignKey(RecordsSport, on_delete=models.CASCADE)
    user = models.ForeignKey('users2.User', on_delete=models.CASCADE)
    time_value = models.DurationField(null=True, blank=True)
    weight_value = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    date_record = models.DateTimeField(null=False)
