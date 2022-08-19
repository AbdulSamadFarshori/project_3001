from django.db import models

# Create your models here.


class Cookies(models.Model):
	set_cookies = models.CharField(max_length=1000)