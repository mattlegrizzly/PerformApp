from django.db import models


class Sport(models.Model):
    name = models.CharField(max_length=100)

class SportsUser(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    user = models.ForeignKey('users2.User', on_delete=models.CASCADE, related_name="sports_user")