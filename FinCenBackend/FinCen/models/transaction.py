from django.db import models
from ..models import *
from ..constants import *


class Transaction(models.Model):
    transaction_id = models.BigAutoField(primary_key=True, serialize=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)
    quantity = models.IntegerField()
    transaction_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)