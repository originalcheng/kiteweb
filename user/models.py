from django.db import models


class User(models.Model):
    username = models.CharField(max_length=64, blank=True)
    firstname = models.CharField(max_length=64, blank=True)
    surname = models.CharField(max_length=64, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=255, db_column='email', unique=True)