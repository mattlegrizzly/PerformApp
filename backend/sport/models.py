from django.db import models
from rest_framework import serializers

class Sport(models.Model):
    name = models.CharField(max_length=100, unique=True)
    isTheme = models.BooleanField(null=True, default=False, unique=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class SportsUser(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    user = models.ForeignKey('users2.User', on_delete=models.CASCADE, related_name="sports_user")

class RecordsGroupSport(models.Model):
    name = models.CharField(max_length=100, unique=False, null=False)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name="group_sports")
    is_general = models.BooleanField(default=False)

    class Meta:
        unique_together = ('name', 'sport')  # Pour éviter les doublons de noms de groupes dans le même sport

class RecordsSport(models.Model):
    UNITS_CHOICE = [
        ('weight', 'Kilogrammes'),
        ('time', 'Temps'),
        ('distance_km', 'Distance en Km'),
        ('distance_m', 'Distance en Mètre'),
        ('points', 'Points'),
        ('reps', 'Répétitions'),
        ('free', 'Personnalisé')
    ]
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    units = models.CharField(max_length=20, choices=UNITS_CHOICE)
    name = models.CharField(max_length=100, unique=False, null=False)
    groups = models.ForeignKey(RecordsGroupSport, null=True, on_delete=models.DO_NOTHING)
    general = models.BooleanField(unique=False, null=True, default=False)
    order = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ['groups__is_general', 'order']  # Ajoute l'ordre de tri par groupe

    def save(self, *args, **kwargs):
        # Assigner un groupe général si aucun groupe n'est défini
        if not self.groups:
            general_group = RecordsGroupSport.objects.filter(is_general=True, sport=self.sport).first()
            if general_group:
                self.groups = general_group

        if self.order is None:  # Si l'ordre n'est pas défini
            # Compter le nombre de records existants dans le même groupe pour le même sport
            existing_records_in_group = RecordsSport.objects.filter(sport=self.sport, groups=self.groups).count()
            # Attribuer l'ordre en conséquence (nombre de records + 1)
            self.order = existing_records_in_group + 1

        super().save(*args, **kwargs)

class RecordsSportUser(models.Model):
    record = models.ForeignKey(RecordsSport, on_delete=models.CASCADE)
    user = models.ForeignKey('users2.User', on_delete=models.CASCADE)
    time_value = models.DurationField(null=True, blank=True)
    record_value = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    free_value = models.CharField(max_length=250, unique=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    date_record = models.DateTimeField(null=False)

    def formatted_record_value(self):
        if self.record_value is not None:
            # Vérification si les décimales sont égales à 0
            if self.record_value % 1 == 0:
                return int(self.record_value)
            return self.record_value
        return None

    def formatted_time_value(self):
        if self.time_value is not None:
            total_seconds = int(self.time_value.total_seconds())
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            milliseconds = self.time_value.microseconds // 1000
            formatted_time = f"{hours:02}:{minutes:02}.{seconds:02}"
            return formatted_time
        return None
    
