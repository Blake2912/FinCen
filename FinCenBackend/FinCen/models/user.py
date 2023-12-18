from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=500, unique=True)
    password_hash = models.CharField(max_length=500)
    email = models.CharField(max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
