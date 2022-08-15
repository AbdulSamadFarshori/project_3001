from django.db import models

# Create your models here.

class main_data(models.Model):
	heading = models.CharField(max_length=255)
	sub_heading = models.CharField(max_length=255)
	main_problem = models.CharField(max_length=6500)
	author_name = models.CharField(max_length=255)

	def __str__(self):
		return self.sub_heading
