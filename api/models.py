from django.db import models

# Create your models here.

class main_data(models.Model):
	id =  models.IntegerField(primary_key=True)
	heading = models.CharField(max_length=255)
	sub_heading = models.CharField(max_length=255)
	main_problem = models.CharField(max_length=6500)
	author_name = models.CharField(max_length=255)

	def __str__(self):
		return self.sub_heading

class response(models.Model):
	case_id = models.ForeignKey(main_data, on_delete=models.CASCADE)
	counsellor = models.CharField(max_length=255)
	petient_asking=models.CharField(max_length=255)
	relavent_score = models.IntegerField()
	summary = models.CharField(max_length=2000)
	reply = models.CharField(max_length=2000)

	def __str__(self):
		return self.case_id

class keywords(models.Model):
	case_id = models.ForeignKey(main_data, on_delete=models.CASCADE)
	keyword = models.CharField(max_length=255)

	def __str__(self):
		return self.case_id

class CompletedCase(models.Model):
	case_id = models.ForeignKey(main_data, on_delete=models.CASCADE)

	def __str__(self):
		return self.case_id


