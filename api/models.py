from django.db import models

# Create your models here.

class main_data(models.Model):
	title = models.CharField(max_length=255)
	sub_heading = models.CharField(max_length=255)
	main_problem = models.CharField(max_length=6500)
	author_name = models.CharField(max_length=255)

	def __str__(self):
		return self.sub_heading

	class Meta:
		verbose_name_plural = "Main Data"

class ReplyData(models.Model):
	case_id = models.ForeignKey(main_data, on_delete=models.CASCADE)
	author = models.CharField(max_length=255)
	recipient = models.CharField(max_length=255)
	reply = models.CharField(max_length=6500)
	

	def __str__(self):
		return self.author

	class Meta:
		verbose_name_plural = "Reply Data"

class ReplyThread(models.Model):
	reply_id = models.ForeignKey(ReplyData, on_delete=models.CASCADE)
	author = models.CharField(max_length=255)
	recipient = models.CharField(max_length=255)
	reply = models.CharField(max_length=6500)
	

	def __str__(self):
		return self.author
		
	class Meta:
		verbose_name_plural = "Reply Thread"

class response(models.Model):
	case_id = models.ForeignKey(main_data, on_delete=models.CASCADE)
	counselor = models.CharField(max_length=255)
	patient_asking = models.CharField(max_length=255)
	patient_need = models.CharField(max_length=255)
	relavent_score = models.IntegerField()
	summary = models.CharField(max_length=2000)
	reply = models.CharField(max_length=2000)

	def __str__(self):
		return self.counselor

	class Meta:
		verbose_name_plural = "Responses"

class keywords(models.Model):
	case_id = models.ForeignKey(main_data, on_delete=models.CASCADE)
	keyword = models.CharField(max_length=255)

	def __str__(self):
		return self.case_id.sub_heading

	class Meta:
		verbose_name_plural = "Keywords"

class CompletedCase(models.Model):
	case_id = models.ForeignKey(main_data, on_delete=models.CASCADE)

	def __str__(self):
		return self.case_id.sub_heading

class LinkConfig(models.Model):
	title = models.CharField(max_length=255)
	heading = models.CharField(max_length=255)
	link = models.CharField(max_length=255)
	main_status = models.CharField(max_length=255)
	reply_status = models.CharField(max_length=255)

	def __str__(self):
		return self.title


class IntentData(models.Model):
	case_id = models.ForeignKey(main_data, on_delete=models.CASCADE)
	intent = models.CharField(max_length=255)

	def __str__(self):
		return self.case_id.sub_heading

	class Meta:
		verbose_name_plural = "Intent Data"

class EntityData(models.Model):
	case_id = models.ForeignKey(main_data, on_delete=models.CASCADE)
	entity = models.CharField(max_length=255)

	def __str__(self):
		return self.case_id.sub_heading

	class Meta:
		verbose_name_plural = "Entity Data"


class Cause(model.Model):
	case_id = models.ForeignKey(main_data, on_delete=models.CASCADE)
	cause = models.CharField(max_length=255)


class CauseKeyword(model.Model):
	case_id = models.ForeignKey(Cause, on_delete=models.CASCADE)
	keyword = models.CharField(max_length=255)