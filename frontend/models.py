from django.db import models

# Create your models here.
class climate(models.Model):
    weather = models.CharField(max_length=40)
    description = models.CharField(max_length=255)
    temp = models.DecimalField(max_digits=6,decimal_places=2,primary_key=True)
    temp_min = models.DecimalField(max_digits=6,decimal_places=2)
    temp_max = models.DecimalField(max_digits=6,decimal_places=2)

class climate_tilicho(models.Model):
    weather = models.CharField(max_length=40)
    description = models.CharField(max_length=255)
    temp = models.DecimalField(max_digits=6,decimal_places=2,primary_key=True)
    temp_min = models.DecimalField(max_digits=6,decimal_places=2)
    temp_max = models.DecimalField(max_digits=6,decimal_places=2)

class climate_langtang(models.Model):
    weather = models.CharField(max_length=40)
    description = models.CharField(max_length=255)
    temp = models.DecimalField(max_digits=6,decimal_places=2,primary_key=True)
    temp_min = models.DecimalField(max_digits=6,decimal_places=2)
    temp_max = models.DecimalField(max_digits=6,decimal_places=2)