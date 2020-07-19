from django.shortcuts import render, redirect 
from Logauth.models import Profile
from django.utils.datastructures import MultiValueDictKeyError
from ChartsGAP.forms import (
	AnalisisGAPDominioUnoForm,
	AnalisisGAPDominioDosForm,
	AnalisisGAPDominioTresForm,
	AnalisisGAPDominioCuatroForm,
	AnalisisGAPDominioCincoForm,
	AnalisisGAPDominioSeisForm,
	AnalisisGAPDominioSieteForm,
	AnalisisGAPDominioOchoForm,
	AnalisisGAPDominioNueveForm,
	AnalisisGAPDominioDiezForm,
	AnalisisGAPDominioOnceForm,
)
from ChartsGAP.models import (
	Subcontrol,
	Control,
	Seccion,
	Dominio,
	Evaluacion,
	Respuesta,
)

def set_por(data):
	TS=0
	CS=0
	TC=0
	CC=0
	TSC=0
	CSS=0
	PC=0
	PNC=0
	CD=0

	for seccion in data['dominio'].seccion.all():
		for control in seccion.control.all():
			for subcontrol in control.subcontrol.all():
				for respuesta in subcontrol.respuesta.all():
					if respuesta.respuesta == True:
						TS+=1
					CS+=1
				if (TS/CS) > 0.5:
					Subcontrol.objects.filter(nombre_subcontrol=subcontrol.nombre_subcontrol).update(total=True)
					TC+=1
					CC+=1
					TSC+=1
					CSS+=1
				else:
					Subcontrol.objects.filter(nombre_subcontrol=subcontrol.nombre_subcontrol).update(total=False)
					CC+=1
					CSS+=1
				
				TS=0
				CS=0

			Control.objects.filter(nombre_control=control.nombre_control).update(porcentaje_cumplimiento=int((TC/CC)*100))
			Control.objects.filter(nombre_control=control.nombre_control).update(porcentaje_no_cumplimiento=int(100 - (TC/CC)*100))

			TC=0
			CC=0

		Seccion.objects.filter(nombre_seccion=seccion.nombre_seccion).update(porcentaje_cumplimiento=int((TSC/CSS)*100))
		Seccion.objects.filter(nombre_seccion=seccion.nombre_seccion).update(porcentaje_no_cumplimiento=int(100 - (TSC/CSS)*100))

		PC+=int((TSC/CSS)*100)
		PNC+=int(100 - (TSC/CSS)*100)

		TSC=0
		CSS=0

		CD+=1

	Dominio.objects.filter(nombre_dominio=data['dominio'].nombre_dominio).update(porcentaje_cumplimiento=int(PC/CD))
	Dominio.objects.filter(nombre_dominio=data['dominio'].nombre_dominio).update(porcentaje_no_cumplimiento=int(PNC/CD))

	return redirect('home')

# Create your views here.

def home(request):
	template_name = "home.html"
	data = {}

	return render(request, template_name, data)

def analisis(request):
	template_name = "analisis.html"
	data = {}

	data['dominio'] = Dominio.objects.all()

	return render(request, template_name, data)

def analisis_uno(request, pk):
	template_name = "analisis1.html"
	data = {}
	data['form'] = AnalisisGAPDominioUnoForm(request.POST or None)
	data['profile'] = request.user
	data['dominio'] = Dominio.objects.get(pk=1)

	if request.method == 'POST':
		if data['form'].is_valid():
			#Subcontrol1
			if data['form'].cleaned_data['respuesta_uno']:
				respuesta_uno = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)

			else:
				respuesta_uno = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol2
			if data['form'].cleaned_data['respuesta_dos']:
				respuesta_dos = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_dos = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)
				

			#Subcontrol3
			if data['form'].cleaned_data['respuesta_tres']:
				respuesta_tres = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_tres = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol4
			if data['form'].cleaned_data['respuesta_cuatro']:
				respuesta_cuatro = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cuatro = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol5
			if data['form'].cleaned_data['respuesta_cinco']:
				respuesta_cinco = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cinco = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol6
			if data['form'].cleaned_data['respuesta_seis']:
				respuesta_seis = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_seis = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol7
			if data['form'].cleaned_data['respuesta_siete']:
				respuesta_siete = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_siete = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			counter=1

			for seccion in data['dominio'].seccion.all():
				for control in seccion.control.all():
					for subcontrol in control.subcontrol.all():
						if counter == 1:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_uno)
						elif counter == 2:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_dos)
						elif counter == 3:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_tres)
						elif counter == 4:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cuatro)
						elif counter == 5:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cinco)
						elif counter == 6:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_seis)
						else:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_siete)
						counter =counter+1

			respuesta_uno.save()
			respuesta_dos.save()
			respuesta_tres.save()
			respuesta_cuatro.save()
			respuesta_cinco.save()
			respuesta_seis.save()
			respuesta_siete.save()

			#Sacando porcentajes
			set_por(data)

			redirect('analisis')

	return render(request, template_name, data)

def analisis_dos(request, pk):
	template_name = "analisis2.html"
	data = {}
	data['form'] = AnalisisGAPDominioDosForm(request.POST or None)
	data['profile'] = request.user
	data['dominio'] = Dominio.objects.get(pk=2)

	if request.method == 'POST':
		if data['form'].is_valid():
			#Subcontrol1
			if data['form'].cleaned_data['respuesta_uno']:
				respuesta_uno = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)

			else:
				respuesta_uno = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol2
			if data['form'].cleaned_data['respuesta_dos']:
				respuesta_dos = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_dos = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)
				

			#Subcontrol3
			if data['form'].cleaned_data['respuesta_tres']:
				respuesta_tres = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_tres = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol4
			if data['form'].cleaned_data['respuesta_cuatro']:
				respuesta_cuatro = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cuatro = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol5
			if data['form'].cleaned_data['respuesta_cinco']:
				respuesta_cinco = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cinco = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol6
			if data['form'].cleaned_data['respuesta_seis']:
				respuesta_seis = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_seis = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol7
			if data['form'].cleaned_data['respuesta_siete']:
				respuesta_siete = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_siete = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol8
			if data['form'].cleaned_data['respuesta_ocho']:
				respuesta_ocho = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_ocho = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol9
			if data['form'].cleaned_data['respuesta_nueve']:
				respuesta_nueve = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_nueve = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol10
			if data['form'].cleaned_data['respuesta_diez']:
				respuesta_diez = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_diez = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol11
			if data['form'].cleaned_data['respuesta_once']:
				respuesta_once = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_once = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			counter=1

			for seccion in data['dominio'].seccion.all():
				for control in seccion.control.all():
					for subcontrol in control.subcontrol.all():
						if counter == 1:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_uno)
						elif counter == 2:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_dos)
						elif counter == 3:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_tres)
						elif counter == 4:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cuatro)
						elif counter == 5:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cinco)
						elif counter == 6:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_seis)
						elif counter == 7:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_siete)
						elif counter == 8:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_ocho)
						elif counter == 9:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_nueve)
						elif counter == 10:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_diez)
						else:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_once)
						counter =counter+1

			respuesta_uno.save()
			respuesta_dos.save()
			respuesta_tres.save()
			respuesta_cuatro.save()
			respuesta_cinco.save()
			respuesta_seis.save()
			respuesta_siete.save()
			respuesta_ocho.save()
			respuesta_nueve.save()
			respuesta_diez.save()
			respuesta_once.save()

			#Sacando porcentajes
			set_por(data)

			redirect('analisis')

	return render(request, template_name, data)

def analisis_tres(request, pk):
	template_name = "analisis3.html"
	data = {}
	data['form'] = AnalisisGAPDominioTresForm(request.POST or None)
	data['profile'] = request.user
	data['dominio'] = Dominio.objects.get(pk=3)

	if request.method == 'POST':
		if data['form'].is_valid():
			#Subcontrol1
			if data['form'].cleaned_data['respuesta_uno']:
				respuesta_uno = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)

			else:
				respuesta_uno = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol2
			if data['form'].cleaned_data['respuesta_dos']:
				respuesta_dos = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_dos = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)
				

			#Subcontrol3
			if data['form'].cleaned_data['respuesta_tres']:
				respuesta_tres = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_tres = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol4
			if data['form'].cleaned_data['respuesta_cuatro']:
				respuesta_cuatro = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cuatro = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol5
			if data['form'].cleaned_data['respuesta_cinco']:
				respuesta_cinco = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cinco = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			counter=1

			for seccion in data['dominio'].seccion.all():
				for control in seccion.control.all():
					for subcontrol in control.subcontrol.all():
						if counter == 1:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_uno)
						elif counter == 2:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_dos)
						elif counter == 3:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_tres)
						elif counter == 4:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cuatro)
						elif counter == 5:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cinco)
						counter =counter+1

			respuesta_uno.save()
			respuesta_dos.save()
			respuesta_tres.save()
			respuesta_cuatro.save()
			respuesta_cinco.save()

			set_por(data)

			redirect('analisis')

	return render(request, template_name, data)

def analisis_cuatro(request, pk):
	template_name = "analisis4.html"
	data = {}
	data['form'] = AnalisisGAPDominioCuatroForm(request.POST or None)
	data['profile'] = request.user
	data['dominio'] = Dominio.objects.get(pk=4)

	if request.method == 'POST':
		if data['form'].is_valid():
			#Subcontrol1
			if data['form'].cleaned_data['respuesta_uno']:
				respuesta_uno = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)

			else:
				respuesta_uno = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol2
			if data['form'].cleaned_data['respuesta_dos']:
				respuesta_dos = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_dos = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)
				

			#Subcontrol3
			if data['form'].cleaned_data['respuesta_tres']:
				respuesta_tres = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_tres = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol4
			if data['form'].cleaned_data['respuesta_cuatro']:
				respuesta_cuatro = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cuatro = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol5
			if data['form'].cleaned_data['respuesta_cinco']:
				respuesta_cinco = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cinco = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol6
			if data['form'].cleaned_data['respuesta_seis']:
				respuesta_seis = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_seis = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol7
			if data['form'].cleaned_data['respuesta_siete']:
				respuesta_siete = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_siete = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol8
			if data['form'].cleaned_data['respuesta_ocho']:
				respuesta_ocho = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_ocho = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol9
			if data['form'].cleaned_data['respuesta_nueve']:
				respuesta_nueve = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_nueve = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol10
			if data['form'].cleaned_data['respuesta_diez']:
				respuesta_diez = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_diez = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			counter=1

			for seccion in data['dominio'].seccion.all():
				for control in seccion.control.all():
					for subcontrol in control.subcontrol.all():
						if counter == 1:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_uno)
						elif counter == 2:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_dos)
						elif counter == 3:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_tres)
						elif counter == 4:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cuatro)
						elif counter == 5:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cinco)
						elif counter == 6:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_seis)
						elif counter == 7:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_siete)
						elif counter == 8:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_ocho)
						elif counter == 9:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_nueve)
						elif counter == 10:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_diez)
						counter =counter+1

			respuesta_uno.save()
			respuesta_dos.save()
			respuesta_tres.save()
			respuesta_cuatro.save()
			respuesta_cinco.save()
			respuesta_seis.save()
			respuesta_siete.save()
			respuesta_ocho.save()
			respuesta_nueve.save()
			respuesta_diez.save()

			set_por(data)

			redirect('analisis')

	return render(request, template_name, data)

def analisis_cinco(request, pk):
	template_name = "analisis5.html"
	data = {}
	data['form'] = AnalisisGAPDominioCincoForm(request.POST or None)
	data['profile'] = request.user
	data['dominio'] = Dominio.objects.get(pk=5)
	if request.method == 'POST':
		if data['form'].is_valid():
			#Subcontrol1
			if data['form'].cleaned_data['respuesta_uno']:
				respuesta_uno = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)

			else:
				respuesta_uno = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol2
			if data['form'].cleaned_data['respuesta_dos']:
				respuesta_dos = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_dos = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)
				

			#Subcontrol3
			if data['form'].cleaned_data['respuesta_tres']:
				respuesta_tres = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_tres = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol4
			if data['form'].cleaned_data['respuesta_cuatro']:
				respuesta_cuatro = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cuatro = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol5
			if data['form'].cleaned_data['respuesta_cinco']:
				respuesta_cinco = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cinco = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol6
			if data['form'].cleaned_data['respuesta_seis']:
				respuesta_seis = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_seis = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol7
			if data['form'].cleaned_data['respuesta_siete']:
				respuesta_siete = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_siete = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol8
			if data['form'].cleaned_data['respuesta_ocho']:
				respuesta_ocho = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_ocho = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol9
			if data['form'].cleaned_data['respuesta_nueve']:
				respuesta_nueve = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_nueve = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol10
			if data['form'].cleaned_data['respuesta_diez']:
				respuesta_diez = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_diez = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol11
			if data['form'].cleaned_data['respuesta_once']:
				respuesta_once = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_once = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol12
			if data['form'].cleaned_data['respuesta_doce']:
				respuesta_doce = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_doce = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol13
			if data['form'].cleaned_data['respuesta_trece']:
				respuesta_trece = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_trece = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol14
			if data['form'].cleaned_data['respuesta_catorce']:
				respuesta_catorce = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_catorce = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol15
			if data['form'].cleaned_data['respuesta_quince']:
				respuesta_quince = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_quince = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol16
			if data['form'].cleaned_data['respuesta_dieciseis']:
				respuesta_dieciseis = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_dieciseis = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol17
			if data['form'].cleaned_data['respuesta_diecisiete']:
				respuesta_diecisiete = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_diecisiete = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol18
			if data['form'].cleaned_data['respuesta_dieciocho']:
				respuesta_dieciocho = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_dieciocho = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol19
			if data['form'].cleaned_data['respuesta_diecinueve']:
				respuesta_diecinueve = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_diecinueve = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol20
			if data['form'].cleaned_data['respuesta_veinte']:
				respuesta_veinte = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veinte = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol21
			if data['form'].cleaned_data['respuesta_veintiuno']:
				respuesta_veintiuno = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veintiuno = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol22
			if data['form'].cleaned_data['respuesta_veintidos']:
				respuesta_veintidos = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veintidos = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			counter=1

			for seccion in data['dominio'].seccion.all():
				for control in seccion.control.all():
					for subcontrol in control.subcontrol.all():
						if counter == 1:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_uno)
						elif counter == 2:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_dos)
						elif counter == 3:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_tres)
						elif counter == 4:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cuatro)
						elif counter == 5:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cinco)
						elif counter == 6:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_seis)
						elif counter == 7:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_siete)
						elif counter == 8:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_ocho)
						elif counter == 9:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_nueve)
						elif counter == 10:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_diez)
						elif counter == 11:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_once)
						elif counter == 12:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_doce)
						elif counter == 13:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_trece)
						elif counter == 14:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_catorce)
						elif counter == 15:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_quince)
						elif counter == 16:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_dieciseis)
						elif counter == 17:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_diecisiete)
						elif counter == 18:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_dieciocho)
						elif counter == 19:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_diecinueve)
						elif counter == 20:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veinte)
						elif counter == 21:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veintiuno)
						else:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veintidos)
						counter =counter+1

			respuesta_uno.save()
			respuesta_dos.save()
			respuesta_tres.save()
			respuesta_cuatro.save()
			respuesta_cinco.save()
			respuesta_seis.save()
			respuesta_siete.save()
			respuesta_ocho.save()
			respuesta_nueve.save()
			respuesta_diez.save()
			respuesta_once.save()
			respuesta_doce.save()
			respuesta_trece.save()
			respuesta_catorce.save()
			respuesta_quince.save()
			respuesta_dieciseis.save()
			respuesta_diecisiete.save()
			respuesta_dieciocho.save()
			respuesta_diecinueve.save()
			respuesta_veinte.save()
			respuesta_veintiuno.save()
			respuesta_veintidos.save()

			set_por(data)

			redirect('analisis')

	return render(request, template_name, data)

def analisis_seis(request, pk):
	template_name = "analisis6.html"
	data = {}
	data['form'] = AnalisisGAPDominioSeisForm(request.POST or None)
	data['profile'] = request.user
	data['dominio'] = Dominio.objects.get(pk=6)
	if request.method == 'POST':
		if data['form'].is_valid():
			#Subcontrol1
			if data['form'].cleaned_data['respuesta_uno']:
				respuesta_uno = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)

			else:
				respuesta_uno = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol2
			if data['form'].cleaned_data['respuesta_dos']:
				respuesta_dos = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_dos = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)
				

			#Subcontrol3
			if data['form'].cleaned_data['respuesta_tres']:
				respuesta_tres = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_tres = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol4
			if data['form'].cleaned_data['respuesta_cuatro']:
				respuesta_cuatro = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cuatro = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol5
			if data['form'].cleaned_data['respuesta_cinco']:
				respuesta_cinco = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cinco = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol6
			if data['form'].cleaned_data['respuesta_seis']:
				respuesta_seis = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_seis = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol7
			if data['form'].cleaned_data['respuesta_siete']:
				respuesta_siete = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_siete = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol8
			if data['form'].cleaned_data['respuesta_ocho']:
				respuesta_ocho = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_ocho = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol9
			if data['form'].cleaned_data['respuesta_nueve']:
				respuesta_nueve = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_nueve = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol10
			if data['form'].cleaned_data['respuesta_diez']:
				respuesta_diez = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_diez = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol11
			if data['form'].cleaned_data['respuesta_once']:
				respuesta_once = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_once = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol12
			if data['form'].cleaned_data['respuesta_doce']:
				respuesta_doce = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_doce = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol13
			if data['form'].cleaned_data['respuesta_trece']:
				respuesta_trece = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_trece = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol14
			if data['form'].cleaned_data['respuesta_catorce']:
				respuesta_catorce = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_catorce = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol15
			if data['form'].cleaned_data['respuesta_quince']:
				respuesta_quince = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_quince = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol16
			if data['form'].cleaned_data['respuesta_dieciseis']:
				respuesta_dieciseis = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_dieciseis = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol17
			if data['form'].cleaned_data['respuesta_diecisiete']:
				respuesta_diecisiete = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_diecisiete = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol18
			if data['form'].cleaned_data['respuesta_dieciocho']:
				respuesta_dieciocho = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_dieciocho = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol19
			if data['form'].cleaned_data['respuesta_diecinueve']:
				respuesta_diecinueve = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_diecinueve = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol20
			if data['form'].cleaned_data['respuesta_veinte']:
				respuesta_veinte = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veinte = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol21
			if data['form'].cleaned_data['respuesta_veintiuno']:
				respuesta_veintiuno = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veintiuno = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol22
			if data['form'].cleaned_data['respuesta_veintidos']:
				respuesta_veintidos = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veintidos = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol23
			if data['form'].cleaned_data['respuesta_veintitres']:
				respuesta_veintitres = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veintitres = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol24
			if data['form'].cleaned_data['respuesta_veinticuatro']:
				respuesta_veinticuatro = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veinticuatro = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol25
			if data['form'].cleaned_data['respuesta_veinticinco']:
				respuesta_veinticinco = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veinticinco = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol26
			if data['form'].cleaned_data['respuesta_veintiseis']:
				respuesta_veintiseis = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veintiseis = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol27
			if data['form'].cleaned_data['respuesta_veintisiete']:
				respuesta_veintisiete = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veintisiete = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol28
			if data['form'].cleaned_data['respuesta_veintiocho']:
				respuesta_veintiocho = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veintiocho = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol29
			if data['form'].cleaned_data['respuesta_veintinueve']:
				respuesta_veintinueve = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veintinueve = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol30
			if data['form'].cleaned_data['respuesta_treinta']:
				respuesta_treinta = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_treinta = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol31
			if data['form'].cleaned_data['respuesta_treintaiuno']:
				respuesta_treintaiuno = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_treintaiuno = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol32
			if data['form'].cleaned_data['respuesta_treintaidos']:
				respuesta_treintaidos = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_treintaidos = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol33
			if data['form'].cleaned_data['respuesta_treintaitres']:
				respuesta_treintaitres = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_treintaitres = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol34
			if data['form'].cleaned_data['respuesta_treintaicuatro']:
				respuesta_treintaicuatro = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_treintaicuatro = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol35
			if data['form'].cleaned_data['respuesta_treintaicinco']:
				respuesta_treintaicinco = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_treintaicinco = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol36
			if data['form'].cleaned_data['respuesta_treintaiseis']:
				respuesta_treintaiseis = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_treintaiseis = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol37
			if data['form'].cleaned_data['respuesta_treintaisiete']:
				respuesta_treintaisiete = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_treintaisiete = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol38
			if data['form'].cleaned_data['respuesta_treintaiocho']:
				respuesta_treintaiocho = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_treintaiocho = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol39
			if data['form'].cleaned_data['respuesta_treintainueve']:
				respuesta_treintainueve = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_treintainueve = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol40
			if data['form'].cleaned_data['respuesta_cuarenta']:
				respuesta_cuarenta = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cuarenta = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol41
			if data['form'].cleaned_data['respuesta_cuarentaiuno']:
				respuesta_cuarentaiuno = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cuarentaiuno = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol42
			if data['form'].cleaned_data['respuesta_cuarentaidos']:
				respuesta_cuarentaidos = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cuarentaidos = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol43
			if data['form'].cleaned_data['respuesta_cuarentaitres']:
				respuesta_cuarentaitres = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cuarentaitres = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol44
			if data['form'].cleaned_data['respuesta_cuarentaicuatro']:
				respuesta_cuarentaicuatro = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cuarentaicuatro = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol45
			if data['form'].cleaned_data['respuesta_cuarentaicinco']:
				respuesta_cuarentaicinco = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cuarentaicinco = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol46
			if data['form'].cleaned_data['respuesta_cuarentaiseis']:
				respuesta_cuarentaiseis = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cuarentaiseis = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol47
			if data['form'].cleaned_data['respuesta_cuarentaisiete']:
				respuesta_cuarentaisiete = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cuarentaisiete = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol48
			if data['form'].cleaned_data['respuesta_cuarentaiocho']:
				respuesta_cuarentaiocho = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cuarentaiocho = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol49
			if data['form'].cleaned_data['respuesta_cuarentainueve']:
				respuesta_cuarentainueve = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cuarentainueve = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)
			counter=1

			for seccion in data['dominio'].seccion.all():
				for control in seccion.control.all():
					for subcontrol in control.subcontrol.all():
						if counter == 1:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_uno)
						elif counter == 2:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_dos)
						elif counter == 3:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_tres)
						elif counter == 4:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cuatro)
						elif counter == 5:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cinco)
						elif counter == 6:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_seis)
						elif counter == 7:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_siete)
						elif counter == 8:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_ocho)
						elif counter == 9:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_nueve)
						elif counter == 10:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_diez)
						elif counter == 11:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_once)
						elif counter == 12:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_doce)
						elif counter == 13:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_trece)
						elif counter == 14:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_catorce)
						elif counter == 15:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_quince)
						elif counter == 16:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_dieciseis)
						elif counter == 17:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_diecisiete)
						elif counter == 18:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_dieciocho)
						elif counter == 19:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_diecinueve)
						elif counter == 20:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veinte)
						elif counter == 21:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veintiuno)
						elif counter == 22:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veintidos)
						elif counter == 23:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veintitres)
						elif counter == 24:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veinticuatro)
						elif counter == 25:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veinticinco)
						elif counter == 26:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veintiseis)
						elif counter == 27:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veintisiete)
						elif counter == 28:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veintiocho)
						elif counter == 29:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veintinueve)
						elif counter == 30:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_treinta)
						elif counter == 31:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_treintaiuno)
						elif counter == 32:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_treintaidos)
						elif counter == 33:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_treintaitres)
						elif counter == 34:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_treintaicuatro)
						elif counter == 35:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_treintaicinco)
						elif counter == 36:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_treintaiseis)
						elif counter == 37:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_treintaisiete)
						elif counter == 38:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_treintaiocho)
						elif counter == 39:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_treintainueve)
						elif counter == 40:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cuarenta)
						elif counter == 41:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cuarentaiuno)
						elif counter == 42:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cuarentaidos)
						elif counter == 43:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cuarentaitres)
						elif counter == 44:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cuarentaicuatro)
						elif counter == 45:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cuarentaicinco)
						elif counter == 46:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cuarentaiseis)
						elif counter == 47:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cuarentaisiete)
						elif counter == 48:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cuarentaiocho)
						else:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cuarentainueve)
						counter =counter+1

			respuesta_uno.save()
			respuesta_dos.save()
			respuesta_tres.save()
			respuesta_cuatro.save()
			respuesta_cinco.save()
			respuesta_seis.save()
			respuesta_siete.save()
			respuesta_ocho.save()
			respuesta_nueve.save()
			respuesta_diez.save()
			respuesta_once.save()
			respuesta_doce.save()
			respuesta_trece.save()
			respuesta_catorce.save()
			respuesta_quince.save()
			respuesta_dieciseis.save()
			respuesta_diecisiete.save()
			respuesta_dieciocho.save()
			respuesta_diecinueve.save()
			respuesta_veinte.save()
			respuesta_veintiuno.save()
			respuesta_veintidos.save()
			respuesta_veintitres.save()
			respuesta_veinticuatro.save()
			respuesta_veinticinco.save()
			respuesta_veintiseis.save()
			respuesta_veintisiete.save()
			respuesta_veintiocho.save()
			respuesta_veintinueve.save()
			respuesta_treinta.save()
			respuesta_treintaiuno.save()
			respuesta_treintaidos.save()
			respuesta_treintaitres.save()
			respuesta_treintaicuatro.save()
			respuesta_treintaicinco.save()
			respuesta_treintaiseis.save()
			respuesta_treintaisiete.save()
			respuesta_treintaiocho.save()
			respuesta_treintainueve.save()
			respuesta_cuarenta.save()
			respuesta_cuarentaiuno.save()
			respuesta_cuarentaidos.save()
			respuesta_cuarentaitres.save()
			respuesta_cuarentaicuatro.save()
			respuesta_cuarentaicinco.save()
			respuesta_cuarentaiseis.save()
			respuesta_cuarentaisiete.save()
			respuesta_cuarentaiocho.save()
			respuesta_cuarentainueve.save()

			set_por(data)

			redirect('analisis')

	return render(request, template_name, data)

def analisis_siete(request, pk):
	template_name = "analisis7.html"
	data = {}
	data['form'] = AnalisisGAPDominioSieteForm(request.POST or None)
	data['profile'] = request.user
	data['dominio'] = Dominio.objects.get(pk=7)
	if request.method == 'POST':
		if data['form'].is_valid():
			#Subcontrol1
			if data['form'].cleaned_data['respuesta_uno']:
				respuesta_uno = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)

			else:
				respuesta_uno = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol2
			if data['form'].cleaned_data['respuesta_dos']:
				respuesta_dos = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_dos = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)
				

			#Subcontrol3
			if data['form'].cleaned_data['respuesta_tres']:
				respuesta_tres = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_tres = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol4
			if data['form'].cleaned_data['respuesta_cuatro']:
				respuesta_cuatro = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cuatro = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol5
			if data['form'].cleaned_data['respuesta_cinco']:
				respuesta_cinco = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cinco = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol6
			if data['form'].cleaned_data['respuesta_seis']:
				respuesta_seis = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_seis = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol7
			if data['form'].cleaned_data['respuesta_siete']:
				respuesta_siete = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_siete = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol8
			if data['form'].cleaned_data['respuesta_ocho']:
				respuesta_ocho = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_ocho = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol9
			if data['form'].cleaned_data['respuesta_nueve']:
				respuesta_nueve = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_nueve = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol10
			if data['form'].cleaned_data['respuesta_diez']:
				respuesta_diez = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_diez = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol11
			if data['form'].cleaned_data['respuesta_once']:
				respuesta_once = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_once = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol12
			if data['form'].cleaned_data['respuesta_doce']:
				respuesta_doce = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_doce = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol13
			if data['form'].cleaned_data['respuesta_trece']:
				respuesta_trece = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_trece = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol14
			if data['form'].cleaned_data['respuesta_catorce']:
				respuesta_catorce = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_catorce = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol15
			if data['form'].cleaned_data['respuesta_quince']:
				respuesta_quince = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_quince = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol16
			if data['form'].cleaned_data['respuesta_dieciseis']:
				respuesta_dieciseis = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_dieciseis = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol17
			if data['form'].cleaned_data['respuesta_diecisiete']:
				respuesta_diecisiete = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_diecisiete = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol18
			if data['form'].cleaned_data['respuesta_dieciocho']:
				respuesta_dieciocho = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_dieciocho = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol19
			if data['form'].cleaned_data['respuesta_diecinueve']:
				respuesta_diecinueve = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_diecinueve = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol20
			if data['form'].cleaned_data['respuesta_veinte']:
				respuesta_veinte = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veinte = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol21
			if data['form'].cleaned_data['respuesta_veintiuno']:
				respuesta_veintiuno = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veintiuno = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol22
			if data['form'].cleaned_data['respuesta_veintidos']:
				respuesta_veintidos = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veintidos = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol23
			if data['form'].cleaned_data['respuesta_veintitres']:
				respuesta_veintitres = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veintitres = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol24
			if data['form'].cleaned_data['respuesta_veinticuatro']:
				respuesta_veinticuatro = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veinticuatro = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol25
			if data['form'].cleaned_data['respuesta_veinticinco']:
				respuesta_veinticinco = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veinticinco = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol26
			if data['form'].cleaned_data['respuesta_veintiseis']:
				respuesta_veintiseis = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veintiseis = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol27
			if data['form'].cleaned_data['respuesta_veintisiete']:
				respuesta_veintisiete = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veintisiete = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol28
			if data['form'].cleaned_data['respuesta_veintiocho']:
				respuesta_veintiocho = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veintiocho = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol29
			if data['form'].cleaned_data['respuesta_veintinueve']:
				respuesta_veintinueve = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veintinueve = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol30
			if data['form'].cleaned_data['respuesta_treinta']:
				respuesta_treinta = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_treinta = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol31
			if data['form'].cleaned_data['respuesta_treintaiuno']:
				respuesta_treintaiuno = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_treintaiuno = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol32
			if data['form'].cleaned_data['respuesta_treintaidos']:
				respuesta_treintaidos = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_treintaidos = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol33
			if data['form'].cleaned_data['respuesta_treintaitres']:
				respuesta_treintaitres = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_treintaitres = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			counter=1

			for seccion in data['dominio'].seccion.all():
				for control in seccion.control.all():
					for subcontrol in control.subcontrol.all():
						if counter == 1:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_uno)
						elif counter == 2:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_dos)
						elif counter == 3:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_tres)
						elif counter == 4:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cuatro)
						elif counter == 5:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cinco)
						elif counter == 6:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_seis)
						elif counter == 7:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_siete)
						elif counter == 8:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_ocho)
						elif counter == 9:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_nueve)
						elif counter == 10:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_diez)
						elif counter == 11:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_once)
						elif counter == 12:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_doce)
						elif counter == 13:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_trece)
						elif counter == 14:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_catorce)
						elif counter == 15:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_quince)
						elif counter == 16:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_dieciseis)
						elif counter == 17:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_diecisiete)
						elif counter == 18:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_dieciocho)
						elif counter == 19:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_diecinueve)
						elif counter == 20:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veinte)
						elif counter == 21:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veintiuno)
						elif counter == 22:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veintidos)
						elif counter == 23:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veintitres)
						elif counter == 24:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veinticuatro)
						elif counter == 25:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veinticinco)
						elif counter == 26:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veintiseis)
						elif counter == 27:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veintisiete)
						elif counter == 28:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veintiocho)
						elif counter == 29:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veintinueve)
						elif counter == 30:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_treinta)
						elif counter == 31:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_treintaiuno)
						elif counter == 32:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_treintaidos)
						else:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_treintaitres)
						counter =counter+1

			respuesta_uno.save()
			respuesta_dos.save()
			respuesta_tres.save()
			respuesta_cuatro.save()
			respuesta_cinco.save()
			respuesta_seis.save()
			respuesta_siete.save()
			respuesta_ocho.save()
			respuesta_nueve.save()
			respuesta_diez.save()
			respuesta_once.save()
			respuesta_doce.save()
			respuesta_trece.save()
			respuesta_catorce.save()
			respuesta_quince.save()
			respuesta_dieciseis.save()
			respuesta_diecisiete.save()
			respuesta_dieciocho.save()
			respuesta_diecinueve.save()
			respuesta_veinte.save()
			respuesta_veintiuno.save()
			respuesta_veintidos.save()
			respuesta_veintitres.save()
			respuesta_veinticuatro.save()
			respuesta_veinticinco.save()
			respuesta_veintiseis.save()
			respuesta_veintisiete.save()
			respuesta_veintiocho.save()
			respuesta_veintinueve.save()
			respuesta_treinta.save()
			respuesta_treintaiuno.save()
			respuesta_treintaidos.save()
			respuesta_treintaitres.save()

			set_por(data)

			redirect('analisis')

	return render(request, template_name, data)

def analisis_ocho(request, pk):
	template_name = "analisis8.html"
	data = {}
	data['form'] = AnalisisGAPDominioOchoForm(request.POST or None)
	data['profile'] = request.user
	data['dominio'] = Dominio.objects.get(pk=8)
	if request.method == 'POST':
		if data['form'].is_valid():
			#Subcontrol1
			if data['form'].cleaned_data['respuesta_uno']:
				respuesta_uno = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)

			else:
				respuesta_uno = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol2
			if data['form'].cleaned_data['respuesta_dos']:
				respuesta_dos = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_dos = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)
				

			#Subcontrol3
			if data['form'].cleaned_data['respuesta_tres']:
				respuesta_tres = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_tres = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol4
			if data['form'].cleaned_data['respuesta_cuatro']:
				respuesta_cuatro = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cuatro = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol5
			if data['form'].cleaned_data['respuesta_cinco']:
				respuesta_cinco = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cinco = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol6
			if data['form'].cleaned_data['respuesta_seis']:
				respuesta_seis = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_seis = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol7
			if data['form'].cleaned_data['respuesta_siete']:
				respuesta_siete = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_siete = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol8
			if data['form'].cleaned_data['respuesta_ocho']:
				respuesta_ocho = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_ocho = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol9
			if data['form'].cleaned_data['respuesta_nueve']:
				respuesta_nueve = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_nueve = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol10
			if data['form'].cleaned_data['respuesta_diez']:
				respuesta_diez = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_diez = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol11
			if data['form'].cleaned_data['respuesta_once']:
				respuesta_once = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_once = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol12
			if data['form'].cleaned_data['respuesta_doce']:
				respuesta_doce = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_doce = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol13
			if data['form'].cleaned_data['respuesta_trece']:
				respuesta_trece = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_trece = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol14
			if data['form'].cleaned_data['respuesta_catorce']:
				respuesta_catorce = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_catorce = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol15
			if data['form'].cleaned_data['respuesta_quince']:
				respuesta_quince = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_quince = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol16
			if data['form'].cleaned_data['respuesta_dieciseis']:
				respuesta_dieciseis = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_dieciseis = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol17
			if data['form'].cleaned_data['respuesta_diecisiete']:
				respuesta_diecisiete = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_diecisiete = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol18
			if data['form'].cleaned_data['respuesta_dieciocho']:
				respuesta_dieciocho = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_dieciocho = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol19
			if data['form'].cleaned_data['respuesta_diecinueve']:
				respuesta_diecinueve = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_diecinueve = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol20
			if data['form'].cleaned_data['respuesta_veinte']:
				respuesta_veinte = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veinte = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol21
			if data['form'].cleaned_data['respuesta_veintiuno']:
				respuesta_veintiuno = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veintiuno = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol22
			if data['form'].cleaned_data['respuesta_veintidos']:
				respuesta_veintidos = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veintidos = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol23
			if data['form'].cleaned_data['respuesta_veintitres']:
				respuesta_veintitres = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veintitres = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol24
			if data['form'].cleaned_data['respuesta_veinticuatro']:
				respuesta_veinticuatro = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veinticuatro = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol25
			if data['form'].cleaned_data['respuesta_veinticinco']:
				respuesta_veinticinco = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veinticinco = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol26
			if data['form'].cleaned_data['respuesta_veintiseis']:
				respuesta_veintiseis = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veintiseis = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol27
			if data['form'].cleaned_data['respuesta_veintisiete']:
				respuesta_veintisiete = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veintisiete = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol28
			if data['form'].cleaned_data['respuesta_veintiocho']:
				respuesta_veintiocho = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veintiocho = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol29
			if data['form'].cleaned_data['respuesta_veintinueve']:
				respuesta_veintinueve = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veintinueve = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol30
			if data['form'].cleaned_data['respuesta_treinta']:
				respuesta_treinta = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_treinta = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol31
			if data['form'].cleaned_data['respuesta_treintaiuno']:
				respuesta_treintaiuno = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_treintaiuno = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol32
			if data['form'].cleaned_data['respuesta_treintaidos']:
				respuesta_treintaidos = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_treintaidos = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol33
			if data['form'].cleaned_data['respuesta_treintaitres']:
				respuesta_treintaitres = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_treintaitres = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			counter=1

			for seccion in data['dominio'].seccion.all():
				for control in seccion.control.all():
					for subcontrol in control.subcontrol.all():
						if counter == 1:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_uno)
						elif counter == 2:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_dos)
						elif counter == 3:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_tres)
						elif counter == 4:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cuatro)
						elif counter == 5:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cinco)
						elif counter == 6:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_seis)
						elif counter == 7:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_siete)
						elif counter == 8:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_ocho)
						elif counter == 9:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_nueve)
						elif counter == 10:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_diez)
						elif counter == 11:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_once)
						elif counter == 12:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_doce)
						elif counter == 13:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_trece)
						elif counter == 14:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_catorce)
						elif counter == 15:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_quince)
						elif counter == 16:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_dieciseis)
						elif counter == 17:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_diecisiete)
						elif counter == 18:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_dieciocho)
						elif counter == 19:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_diecinueve)
						elif counter == 20:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veinte)
						elif counter == 21:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veintiuno)
						elif counter == 22:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veintidos)
						elif counter == 23:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veintitres)
						elif counter == 24:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veinticuatro)
						elif counter == 25:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veinticinco)
						elif counter == 26:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veintiseis)
						elif counter == 27:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veintisiete)
						elif counter == 28:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veintiocho)
						elif counter == 29:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veintinueve)
						elif counter == 30:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_treinta)
						elif counter == 31:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_treintaiuno)
						elif counter == 32:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_treintaidos)
						else:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_treintaitres)
						counter =counter+1

			respuesta_uno.save()
			respuesta_dos.save()
			respuesta_tres.save()
			respuesta_cuatro.save()
			respuesta_cinco.save()
			respuesta_seis.save()
			respuesta_siete.save()
			respuesta_ocho.save()
			respuesta_nueve.save()
			respuesta_diez.save()
			respuesta_once.save()
			respuesta_doce.save()
			respuesta_trece.save()
			respuesta_catorce.save()
			respuesta_quince.save()
			respuesta_dieciseis.save()
			respuesta_diecisiete.save()
			respuesta_dieciocho.save()
			respuesta_diecinueve.save()
			respuesta_veinte.save()
			respuesta_veintiuno.save()
			respuesta_veintidos.save()
			respuesta_veintitres.save()
			respuesta_veinticuatro.save()
			respuesta_veinticinco.save()
			respuesta_veintiseis.save()
			respuesta_veintisiete.save()
			respuesta_veintiocho.save()
			respuesta_veintinueve.save()
			respuesta_treinta.save()
			respuesta_treintaiuno.save()
			respuesta_treintaidos.save()
			respuesta_treintaitres.save()

			set_por(data)

			redirect('analisis')

	return render(request, template_name, data)

def analisis_nueve(request, pk):
	template_name = "analisis9.html"
	data = {}
	data['form'] = AnalisisGAPDominioNueveForm(request.POST or None)
	data['profile'] = request.user
	data['dominio'] = Dominio.objects.get(pk=9)
	if request.method == 'POST':
		if data['form'].is_valid():
			#Subcontrol1
			if data['form'].cleaned_data['respuesta_uno']:
				respuesta_uno = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)

			else:
				respuesta_uno = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol2
			if data['form'].cleaned_data['respuesta_dos']:
				respuesta_dos = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_dos = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)
				

			#Subcontrol3
			if data['form'].cleaned_data['respuesta_tres']:
				respuesta_tres = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_tres = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol4
			if data['form'].cleaned_data['respuesta_cuatro']:
				respuesta_cuatro = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cuatro = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol5
			if data['form'].cleaned_data['respuesta_cinco']:
				respuesta_cinco = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cinco = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol6
			if data['form'].cleaned_data['respuesta_seis']:
				respuesta_seis = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_seis = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol7
			if data['form'].cleaned_data['respuesta_siete']:
				respuesta_siete = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_siete = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol8
			if data['form'].cleaned_data['respuesta_ocho']:
				respuesta_ocho = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_ocho = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol9
			if data['form'].cleaned_data['respuesta_nueve']:
				respuesta_nueve = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_nueve = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol10
			if data['form'].cleaned_data['respuesta_diez']:
				respuesta_diez = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_diez = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol11
			if data['form'].cleaned_data['respuesta_once']:
				respuesta_once = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_once = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			counter=1

			for seccion in data['dominio'].seccion.all():
				for control in seccion.control.all():
					for subcontrol in control.subcontrol.all():
						if counter == 1:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_uno)
						elif counter == 2:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_dos)
						elif counter == 3:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_tres)
						elif counter == 4:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cuatro)
						elif counter == 5:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cinco)
						elif counter == 6:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_seis)
						elif counter == 7:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_siete)
						elif counter == 8:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_ocho)
						elif counter == 9:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_nueve)
						elif counter == 10:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_diez)
						elif counter == 11:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_once)
						counter =counter+1

			respuesta_uno.save()
			respuesta_dos.save()
			respuesta_tres.save()
			respuesta_cuatro.save()
			respuesta_cinco.save()
			respuesta_seis.save()
			respuesta_siete.save()
			respuesta_ocho.save()
			respuesta_nueve.save()
			respuesta_diez.save()
			respuesta_once.save()

			set_por(data)

			redirect('analisis')

	return render(request, template_name, data)

def analisis_diez(request, pk):
	template_name = "analisis10.html"
	data = {}
	data['form'] = AnalisisGAPDominioDiezForm(request.POST or None)
	data['profile'] = request.user
	data['dominio'] = Dominio.objects.get(pk=10)
	if request.method == 'POST':
		if data['form'].is_valid():
			#Subcontrol1
			if data['form'].cleaned_data['respuesta_uno']:
				respuesta_uno = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)

			else:
				respuesta_uno = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol2
			if data['form'].cleaned_data['respuesta_dos']:
				respuesta_dos = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_dos = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)
				

			#Subcontrol3
			if data['form'].cleaned_data['respuesta_tres']:
				respuesta_tres = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_tres = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol4
			if data['form'].cleaned_data['respuesta_cuatro']:
				respuesta_cuatro = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cuatro = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol5
			if data['form'].cleaned_data['respuesta_cinco']:
				respuesta_cinco = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cinco = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol6
			if data['form'].cleaned_data['respuesta_seis']:
				respuesta_seis = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_seis = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol7
			if data['form'].cleaned_data['respuesta_siete']:
				respuesta_siete = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_siete = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol8
			if data['form'].cleaned_data['respuesta_ocho']:
				respuesta_ocho = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_ocho = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol9
			if data['form'].cleaned_data['respuesta_nueve']:
				respuesta_nueve = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_nueve = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol10
			if data['form'].cleaned_data['respuesta_diez']:
				respuesta_diez = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_diez = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol11
			if data['form'].cleaned_data['respuesta_once']:
				respuesta_once = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_once = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			counter=1

			for seccion in data['dominio'].seccion.all():
				for control in seccion.control.all():
					for subcontrol in control.subcontrol.all():
						if counter == 1:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_uno)
						elif counter == 2:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_dos)
						elif counter == 3:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_tres)
						elif counter == 4:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cuatro)
						elif counter == 5:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cinco)
						elif counter == 6:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_seis)
						elif counter == 7:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_siete)
						elif counter == 8:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_ocho)
						elif counter == 9:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_nueve)
						else:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_diez)
						counter =counter+1

			respuesta_uno.save()
			respuesta_dos.save()
			respuesta_tres.save()
			respuesta_cuatro.save()
			respuesta_cinco.save()
			respuesta_seis.save()
			respuesta_siete.save()
			respuesta_ocho.save()
			respuesta_nueve.save()
			respuesta_diez.save()

			set_por(data)

			redirect('analisis')

	return render(request, template_name, data)

def analisis_once(request, pk):
	template_name = "analisis11.html"
	data = {}
	data['form'] = AnalisisGAPDominioOnceForm(request.POST or None)
	data['profile'] = request.user
	data['dominio'] = Dominio.objects.get(pk=11)
	data['analisis'] = Evaluacion.objects.all()
	if request.method == 'POST':
		if data['form'].is_valid():
			#Subcontrol1
			if data['form'].cleaned_data['respuesta_uno']:
				respuesta_uno = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)

			else:
				respuesta_uno = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol2
			if data['form'].cleaned_data['respuesta_dos']:
				respuesta_dos = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_dos = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)
				

			#Subcontrol3
			if data['form'].cleaned_data['respuesta_tres']:
				respuesta_tres = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_tres = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol4
			if data['form'].cleaned_data['respuesta_cuatro']:
				respuesta_cuatro = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cuatro = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol5
			if data['form'].cleaned_data['respuesta_cinco']:
				respuesta_cinco = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_cinco = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol6
			if data['form'].cleaned_data['respuesta_seis']:
				respuesta_seis = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_seis = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol7
			if data['form'].cleaned_data['respuesta_siete']:
				respuesta_siete = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_siete = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol8
			if data['form'].cleaned_data['respuesta_ocho']:
				respuesta_ocho = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_ocho = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol9
			if data['form'].cleaned_data['respuesta_nueve']:
				respuesta_nueve = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_nueve = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol10
			if data['form'].cleaned_data['respuesta_diez']:
				respuesta_diez = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_diez = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol11
			if data['form'].cleaned_data['respuesta_once']:
				respuesta_once = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_once = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol12
			if data['form'].cleaned_data['respuesta_doce']:
				respuesta_doce = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_doce = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol13
			if data['form'].cleaned_data['respuesta_trece']:
				respuesta_trece = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_trece = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol14
			if data['form'].cleaned_data['respuesta_catorce']:
				respuesta_catorce = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_catorce = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol15
			if data['form'].cleaned_data['respuesta_quince']:
				respuesta_quince = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_quince = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol16
			if data['form'].cleaned_data['respuesta_dieciseis']:
				respuesta_dieciseis = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_dieciseis = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol17
			if data['form'].cleaned_data['respuesta_diecisiete']:
				respuesta_diecisiete = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_diecisiete = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol18
			if data['form'].cleaned_data['respuesta_dieciocho']:
				respuesta_dieciocho = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_dieciocho = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol19
			if data['form'].cleaned_data['respuesta_diecinueve']:
				respuesta_diecinueve = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_diecinueve = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol20
			if data['form'].cleaned_data['respuesta_veinte']:
				respuesta_veinte = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veinte = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			#Subcontrol21
			if data['form'].cleaned_data['respuesta_veintiuno']:
				respuesta_veintiuno = Respuesta.objects.create(
					respuesta=True,
					autor=data['profile'].profile,
				)
				
			else:
				respuesta_veintiuno = Respuesta.objects.create(
					respuesta=False,
					autor=data['profile'].profile,
				)

			counter=1

			for seccion in data['dominio'].seccion.all():
				for control in seccion.control.all():
					for subcontrol in control.subcontrol.all():
						if counter == 1:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_uno)
						elif counter == 2:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_dos)
						elif counter == 3:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_tres)
						elif counter == 4:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cuatro)
						elif counter == 5:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_cinco)
						elif counter == 6:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_seis)
						elif counter == 7:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_siete)
						elif counter == 8:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_ocho)
						elif counter == 9:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_nueve)
						elif counter == 10:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_diez)
						elif counter == 11:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_once)
						elif counter == 12:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_doce)
						elif counter == 13:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_trece)
						elif counter == 14:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_catorce)
						elif counter == 15:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_quince)
						elif counter == 16:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_dieciseis)
						elif counter == 17:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_diecisiete)
						elif counter == 18:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_dieciocho)
						elif counter == 19:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_diecinueve)
						elif counter == 20:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veinte)
						else:
							Subcontrol.objects.get(nombre_subcontrol=subcontrol.nombre_subcontrol).respuesta.add(respuesta_veintiuno)
						counter =counter+1

			respuesta_uno.save()
			respuesta_dos.save()
			respuesta_tres.save()
			respuesta_cuatro.save()
			respuesta_cinco.save()
			respuesta_seis.save()
			respuesta_siete.save()
			respuesta_ocho.save()
			respuesta_nueve.save()
			respuesta_diez.save()
			respuesta_once.save()
			respuesta_doce.save()
			respuesta_trece.save()
			respuesta_catorce.save()
			respuesta_quince.save()
			respuesta_dieciseis.save()
			respuesta_diecisiete.save()
			respuesta_dieciocho.save()
			respuesta_diecinueve.save()
			respuesta_veinte.save()
			respuesta_veintiuno.save()

			set_por(data)

			total=0
			contador=0

			for porcentaje in data['analisis'].dominio.all():
				total+= porcentaje.porcentaje_cumplimiento
				contador+=1
			Evento.objects.filter(pk=0).update(porcentaje_cumplimiento=int(total/contador))
			Evento.objects.filter(pk=0).update(porcentaje_no_cumplimiento=int(100 - (total/contador)))


			redirect('analisis')

	return render(request, template_name, data)