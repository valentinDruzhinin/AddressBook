from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
