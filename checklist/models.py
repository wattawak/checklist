from django.db import models

class Task(models.Model):
	title = models.CharField(max_length=250, unique=True)
	description = models.CharField(max_length=1000)
	due_date = models.DateTimeField()
	is_complete = models.BooleanField(default=False)

	def __str__(self):
		return self.title



