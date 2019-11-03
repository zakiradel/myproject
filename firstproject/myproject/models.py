from django.db import models

class Info(models.Model):
	name = models.CharField(max_length=200)
	phone = models.IntegerField(null=True, blank=True)
	email = models.EmailField()
	address = models.CharField(max_length=200)
	photo = models.ImageField()

	def __str__(self):
		return self.name
