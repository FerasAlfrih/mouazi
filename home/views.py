from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import  AuthenticationForm

def home(request, resource):
		form =AuthenticationForm(request.POST)
		
		# if request.method == 'POST':
		# 	username = request.POST['username']
		# 	password = request.POST['password']
		# 	if User.objects.filter(username=username):
		# 		user=User.objects.get(username=username)			
		# 		auth = authenticate(request, username=username, password=password)
		# 		if auth is not None:
		# 			login(request, auth)
		# 			messages.success(request, f'Welcome Back {username}')
		# 			print(user.username)					
		# 		else:
		# 			messages.warning(request, f'Check your username and passowrd and try again please')
		# 		return render (request,'home/home.html', {'form':form})
		# 	else:
		# 		user = ""
		# 		messages.warning(request, f'No such u username in our database, check your spelling please')
		# else:  
		# 	messages.success(request,f'GET Method')  
		context ={
			'form':form,
			
		}	
		return render (request,'home/home.html', context)
