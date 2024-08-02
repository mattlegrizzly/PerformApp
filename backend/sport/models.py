from django.db import models


class Sport(models.Model):
    name = models.CharField(max_length=100, unique=True)
    isTheme = models.BooleanField(null=True, default=False, unique=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class SportsUser(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    user = models.ForeignKey('users2.User', on_delete=models.CASCADE, related_name="sports_user")

class RecordsGroupSport(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)

class RecordsSport(models.Model):
    UNITS_CHOICE = [
        ('weight', 'Kilogrammes'),
        ('time', 'Temps'),
        ('distance_km', 'Distance en Km'),
        ('distance_m', 'Distance en Mètre'),
        ('points', 'Points'),
        ('free', 'Personnalisé')
    ]
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    units = models.CharField(max_length=20, choices=UNITS_CHOICE)
    name = models.CharField(max_length=100, unique=False, null=False)
    groups = models.ForeignKey(RecordsGroupSport, unique=True, null=True, on_delete=models.DO_NOTHING)
    general = models.BooleanField(unique=False, null=True, default=False)
    order = models.PositiveIntegerField(null=True, blank=True)
    class Meta:
        ordering = ['order']

    def save(self, *args, **kwargs):
        if self.order is None:  # Si l'ordre n'est pas défini
            # Compter le nombre de records existants pour le même sport
            existing_records = RecordsSport.objects.filter(sport=self.sport).count()
            # Attribuer l'ordre en conséquence (nombre de records + 1)
            self.order = existing_records + 1

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
    
