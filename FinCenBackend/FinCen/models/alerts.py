from django.db import models
from ..models import *
from ..constants import *

class Alerts(models.Model):
    alert_id = models.BigAutoField(primary_key=True, serialize=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    condition = models.CharField(max_length=500)
    trigger_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_triggered = models.BooleanField()