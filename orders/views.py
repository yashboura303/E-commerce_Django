from django.shortcuts import render
from products.models import Products
from cart.models import Cart
from .models import Orders
from django.core import serializers
import datetime

def orderPage(request):
    orders, created = Orders.objects.get_or_create(customer=request.user)
    cartProducts = Cart.objects.get(customer=request.user).products.all()
    orders.products.set(cartProducts)
    orders.save()
    if orders.date_ordered == None:
        orders.date_ordered = datetime.datetime.now()
        orders.save()
    else:
        pass
    
    #delete cart products after buying
    cart = Cart.objects.get(customer=request.user)
    for product in cartProducts:
        cart.products.remove(product)
    return render(request,'orders/order.html',{"products":orders.products.all(),"order":orders})

