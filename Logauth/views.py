from django.shortcuts import render, redirect 
from django.contrib import auth, messages
from django.contrib.auth.models import User
from Logauth.models import Profile
from Logauth.forms import ProfileForm
from django.db import IntegrityError
from django.core.exceptions import ValidationError

# Create your views here.

def login(request):
	template_name = "login.html"
	data = {}

	if request.POST:
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(
			username=username,
			password=password,
		)

		if user is not None:
			if user.is_active:
				auth.login(request, user)
				return redirect('home')
			else:
				messages.add_message(
					request,
					messages.ERROR,
					'Usuario o contraseña incorrecta',
					)
		else:
			messages.add_message(
				request,
				messages.ERROR,
				'Usuario o contraseña incorrecta',
				)

	return render(request, template_name, data)

def logout(request):
	auth.logout(request)
	return redirect('login')

def register(request):
	template_name = 'register.html'

	data = {}

	data['form'] = ProfileForm(request.POST or None)

	if request.method == 'POST':
		if data['form'].is_valid():
			try:
				user = User.objects.create_user(
					username=request.POST['username'],
					password=request.POST['password'],
				)

				profile = Profile.objects.create(
					user=user,
					age=request.POST['age'],
					email=request.POST['email'],
					rut=request.POST['rut'],
					primer_nombre=request.POST['primer_nombre'],
					segundo_nombre=request.POST['segundo_nombre'],
					apellido_paterno=request.POST['apellido_paterno'],
					apellido_materno=request.POST['apellido_materno'],
					cargo=request.POST['cargo'],
					departamento=request.POST['departamento'],
					sucursal=request.POST['sucursal'],
				)

				user.save()
				profile.save()

				messages.add_message(
					request,
					messages.SUCCESS,
					'Usuario creado exitosamente'
				)

				return redirect('login')
			except IntegrityError as ie:
				messages.add_message(
					request,
					messages.ERROR,
					'Hubieron problemas creando al usuario ERROR: {error}'.format(error=str(ie))
				)
			except ValidationError as ve:
				messages.add_message(
					request,
					messages.ERROR,
					'Hubieron problemas creando al usuario ERROR: {error}'.format(error=str(ve))
				)
		else:
			messages.add_message(
				request,
				messages.ERROR,
				'Hubieron problemas creando al usuario'
			)

	return render(request, template_name, data)