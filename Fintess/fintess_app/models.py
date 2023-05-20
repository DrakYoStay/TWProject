from django.db import models
from django.contrib.auth.models import User

class InputValue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Value: {self.value}, Date: {self.date}"