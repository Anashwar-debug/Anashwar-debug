from django.db import models
from datetime import datetime

class posts(models.Model):
    title=models.CharField(max_length=500)
    Body=models.CharField(max_length=1000000)
    created_at=models.DateField(default=datetime.now(),blank=True)

# Create your models here.
