from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=500, unique=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    password_hash = models.CharField(max_length=500)
    email = models.CharField(max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_activated = models.BooleanField()
