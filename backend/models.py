from django.db import models

# Create your models here.
class Weather(models.Model):
    Temperature = models.FloatField()
    Humidity = models.FloatField()
    Weather = models.CharField(max_length=10)
    Season = models.CharField(max_length=10)
