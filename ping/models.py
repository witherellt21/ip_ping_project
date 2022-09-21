from django.db import models
from django.utils import timezone

class ip_address(models.Model):
    ip_address = models.CharField(max_length = 15)
    timestamp = models.DateTimeField(default=timezone.now)
