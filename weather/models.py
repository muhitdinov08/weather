from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


class Abstract(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Weather(Abstract):
    author = models.ManyToManyField(User)
    city_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.city_name
