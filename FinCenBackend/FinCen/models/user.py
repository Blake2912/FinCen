from django.db import models
from django.contrib.auth.hashers import make_password
from ..util import CommonUtil

class User(models.Model):
    user_name = models.CharField(max_length=500, unique=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    password = models.CharField(max_length=500)
    email = models.CharField(max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_activated = models.BooleanField(default=False)
    api_key = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        self.api_key = CommonUtil.generate_api_key() 
        super(User, self).save(*args, **kwargs)
