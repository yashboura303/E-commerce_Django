from django.shortcuts import render,redirect,get_object_or_404
from .models import Products
from cart.models import Cart
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
	products = Products.objects
	return render(request, 'products/home.html',{'products': products})

def add_cart(request, product_id):
	if request.user.pk:
		user = User.objects.get(pk = request.user.pk)
		cart, created = Cart.objects.get_or_create(customer = request.user)
		cart.customer = user 
		cart.save()
		product = get_object_or_404(Products, pk = product_id )
		cart.products.add(product)
		cart.total_price += product.price
		cart.save()
		messages.success(request,f"{product.title} added to your cart !")
		return redirect('home')
	else:
		messages.warning(request, "Please login to add products to the cart")
		return redirect('home')

def search(request):
	products = Products.objects

	if "Productcategory" in request.GET:
		productCategory = request.GET["Productcategory"]
		products = products.filter(category__icontains = productCategory)
		
		
	if "searchInput" in request.GET:
		searchInput = request.GET["searchInput"]
		products = products.filter(title__icontains= searchInput)

	
	
	return render(request, 'products/home.html',{'products': products,'values':request.GET})