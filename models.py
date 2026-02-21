from django.db import models
from fleet.models import Vehicle

class ServiceLog(models.Model):

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    description = models.TextField()
    cost = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.vehicle.status = 'in_shop'
        self.vehicle.save()
        super().save(*args, **kwargs)

class FuelLog(models.Model):

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    liters = models.FloatField()
    cost = models.FloatField()
    date = models.DateField(auto_now_add=True)