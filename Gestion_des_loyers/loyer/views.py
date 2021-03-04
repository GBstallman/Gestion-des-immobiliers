from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login ,authenticate,logout

from .models import *

def login(request):

	if request.method == 'POST' :
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username,password=password)

		if user is not None:
			auth_login(request, user)
			return redirect('home')

		else:
			messages.info(request,'Username or Password is incorrect')
	context = {}
	return render(request,'loyer/login.html',context)


def logout(request):
	pass

def home(request):
	context = {}
	return render(request,'loyer/index.html',context)


def office(request):
	context = {}
	return render(request,'loyer/office.html',context)


def tenant(request):
	context = {}
	return render(request,'loyer/tenant.html',context)

def calendar(request):
	context = {}
	return render(request,'loyer/calendar.html',context)