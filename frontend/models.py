from dataclasses import field
from django.db import models

# Create your models here.
class climate(models.Model):
    weather = models.CharField(max_length=40)
    description = models.CharField(max_length=255)
    temp = models.DecimalField(max_digits=6,decimal_places=2,primary_key=True)
    temp_min = models.DecimalField(max_digits=6,decimal_places=2)
    temp_max = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.weather

class climate_tilicho(models.Model):
    weather = models.CharField(max_length=40)
    description = models.CharField(max_length=255)
    temp = models.DecimalField(max_digits=6,decimal_places=2,primary_key=True)
    temp_min = models.DecimalField(max_digits=6,decimal_places=2)
    temp_max = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.weather

class climate_langtang(models.Model):
    weather = models.CharField(max_length=40)
    description = models.CharField(max_length=255)
    temp = models.DecimalField(max_digits=6,decimal_places=2,primary_key=True)
    temp_min = models.DecimalField(max_digits=6,decimal_places=2)
    temp_max = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.weather

class sensor_tempreture(models.Model):
    created_at = models.CharField(max_length=40,primary_key=True)
    field1 = models.DecimalField(max_digits=6,decimal_places=2)
    field2 = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.field1