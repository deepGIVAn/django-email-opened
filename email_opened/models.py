from django.db import models

class EmailLog(models.Model):
    email_id = models.CharField(max_length=255, unique=True)
    opened = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)
