from django.shortcuts import render,redirect
from products.models import Products
from .models import Cart
from orders.models import Orders

def cart(request):
	cart = Cart.objects.get(customer=request.user)
	if cart.products.exists():
		pass
	else:
		cart.total_price = 0
		cart.save()

	return render(request,'cart/cart_page.html',{ 'cart': cart, 'total_price':cart.total_price})

def delete_cart(request,product_id):
	cart = Cart.objects.get(customer=request.user)
	product = Products.objects.get(id=product_id)
	cart.total_price = cart.total_price - product.price
	cart.save()
	cart.products.remove(product)
	return redirect('cart')


