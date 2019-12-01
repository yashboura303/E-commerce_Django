from django.db import models
from django.contrib.auth.models import User
from products.models import Products
# Create your models here.
class Orders(models.Model):
    customer = models.OneToOneField(User, on_delete = models.CASCADE,null = True)
    products = models.ManyToManyField(Products,blank = True)
    date_ordered = models.DateTimeField(null = True)
    def __str__(self):
        return f"{self.customer} Order"