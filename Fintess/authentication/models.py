from django.db import models
from django.contrib.auth.models import User

class WeightEntry(models.Model):
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)