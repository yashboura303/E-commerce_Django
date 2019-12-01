from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth,messages
from cart.models import Cart
import re 


def login(request):
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
		if user is not None:
			auth.login(request,user)
			return redirect('home')
		else:
			messages.error(request, 'Invalid credentials')
			return redirect('login')
	return render (request, 'accounts/login.html')

def signup(request):
    if request.method == 'POST':
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                if user:
                    messages.error(request, 'Username already exists!')
                    return render(request, 'accounts/signup.html')
                if not re.search(regex,request.POST['email']):
                    messages.error(request, 'Enter Valid Email!')
                    return render(request, 'accounts/signup.html')

            except User.DoesNotExist:
	            user = User.objects.create_user(request.POST['username'], email= request.POST['email'],password=request.POST['password1'])
	            auth.login(request,user)
	            return redirect('home')
        else:
        	messages.error(request,'Passwords should match')
        	return render(request, 'accounts/signup.html')
    else:
  	      return render(request, 'accounts/signup.html')

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('home')
