from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('manager', 'Fleet Manager'),
        ('dispatcher', 'Dispatcher'),
        ('safety', 'Safety Officer'),
        ('finance', 'Financial Analyst'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)