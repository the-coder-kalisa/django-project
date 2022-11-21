from django.db import models
from django.utils.timezone import now


class Tasks(models.Model):
    name = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=now)
    status = models.CharField(max_length=1000000, default="pending")
