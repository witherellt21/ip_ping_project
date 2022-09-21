from django.db import models

class ip_address(models.Model):
    ip_address = models.CharField(max_length = 15)
    timestamp = models.DateTimeField('timestamp')
