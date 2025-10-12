"""
Don't forget that after you make a change in a model class,
such as deleting a property, or renaming a property, or adding
a new model, etc., you need to create a migration and run 
migrations as well.

Run the following command to create a migration (run this after you make
you change in this file):

  python3 manage.py makemigrations

This will create a file in the `migrations` folder. After the migration
file is create you'll need to run the migrations with the following command:

  python3 manage.py migrate
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image =models.ImageField(upload_to='', null=True)
    caption = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)