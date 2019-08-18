from django.contrib import admin
from .models import HouseInformation, PredictionLog

# Register your models here.

admin.site.register(HouseInformation)
admin.site.register(PredictionLog)
