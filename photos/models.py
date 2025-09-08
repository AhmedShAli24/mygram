from django.db import models

class User(models.Model):
    email = models.CharField(max_length=200)

class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=200)