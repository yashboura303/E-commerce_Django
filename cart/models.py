from django.db import models
from django.contrib.auth.models import User
from products.models import Products

class Cart(models.Model):
	total_price = models.IntegerField(default = 0)
	customer = models.OneToOneField(User, on_delete = models.CASCADE,null = True)
	products = models.ManyToManyField(Products,blank = True)
	is_ordered = models.BooleanField(default = False)	

	def __str__(self):
		return  "{}".format(self.customer)