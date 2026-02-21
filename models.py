from django.db import models
from fleet.models import Vehicle
from django.conf import settings

class Driver(models.Model):

    STATUS = (
        ('on_duty', 'On Duty'),
        ('off_duty', 'Off Duty'),
        ('suspended', 'Suspended'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=50)
    license_expiry = models.DateField()
    safety_score = models.FloatField(default=100)
    status = models.CharField(max_length=20, choices=STATUS, default='off_duty')

    def __str__(self):
        return self.user.username

class Trip(models.Model):

    STATUS = (
        ('draft', 'Draft'),
        ('dispatched', 'Dispatched'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    cargo_weight = models.FloatField()
    start_odometer = models.FloatField()
    end_odometer = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='draft')

    def save(self, *args, **kwargs):
        if self.cargo_weight > self.vehicle.max_capacity:
            raise ValueError("Cargo exceeds vehicle capacity!")
        super().save(*args, **kwargs)