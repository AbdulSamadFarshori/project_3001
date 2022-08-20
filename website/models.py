from django.db import models
from django.utils.timezone import now
from datetime import datetime

# Create your models here.

class Cookies(models.Model):
	set_cookies = models.CharField(max_length=1000)

class FingerPrints(models.Model):
	date_time = models.DateTimeField(default=datetime.now, editable=False)
	ip = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
