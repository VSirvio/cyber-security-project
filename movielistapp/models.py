from django.contrib.auth.models import User
from django.db import models

class Movie(models.Model):
    title = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
