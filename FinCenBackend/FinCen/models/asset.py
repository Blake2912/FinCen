from django.db import models
from .user import *
from ..constants.db_constants import * 


class Asset(models.Model):
    asset_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=200)
    asset_type = models.CharField(max_length=10, choices=ASSET_TYPES)
    quantity = models.IntegerField()
    purchase_price = models.FloatField()
    purchase_datetime = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)