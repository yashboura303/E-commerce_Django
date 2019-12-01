from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
	title = models.CharField(max_length = 100)
	body = models.TextField(null = True)
	description = models.TextField(null = True)
	price = models.IntegerField(null = True)
	image = models.ImageField(upload_to = 'images/')
	category = models.CharField(max_length = 50)

	def __str__(self):
		return self.title



