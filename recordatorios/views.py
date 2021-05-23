from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError

def home(request):
	return render(request, 'recordatorios/home.html')

def registro(request):
	if request.method == 'GET':
		return render(request, 'recordatorios/registro.html', {'form':UserCreationForm()})
	else:
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
				user.save()
				login(request, user)
				return redirect('recordatorios')
			except IntegrityError:
				return render(request, 'recordatorios/registro.html', {'form':UserCreationForm(), 'error':'El usuario ya existe, favor de elegir uno nuevo.'})
		else:
			return render(request, 'recordatorios/registro.html', {'form':UserCreationForm(),'error':UserCreationForm().error_messages['password_mismatch']})

def iniciarsesion(request):
	if request.method == 'GET':
		return render(request, 'recordatorios/iniciarsesion.html', {'form':AuthenticationForm()})
	else:
		user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
		if user is None:
			return render(request, 'recordatorios/iniciarsesion.html', {'form':AuthenticationForm(),'error':'El usuario y/o contraseñas son incorrectos.'})
		else:
			login(request, user)
			return redirect('home')
		
def cerrarsesion(request):
	if request.method == 'POST':
		logout(request)
		return render(request, 'recordatorios/home.html')
	else:
		return render(request, 'recordatorios/home.html')

def recordatorios(request):
	return render(request, 'recordatorios/recordatorios.html')