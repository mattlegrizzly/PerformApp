from django.contrib import admin
from .models import Sport

class SportAdmin(admin.ModelAdmin):
    pass


admin.site.register(Sport, SportAdmin)