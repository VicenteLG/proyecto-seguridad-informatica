from django.shortcuts import render
from ChartsGAP.models import (
	Dominio,
)


# Create your views here.

def encuesta(request):
	template_name = 'encuesta.html'
	data = {}

	data['dominio_uno'] = Dominio.objects.get(pk=1)
	data['dominio_dos'] = Dominio.objects.get(pk=2)
	data['dominio_tres'] = Dominio.objects.get(pk=3)
	data['dominio_cuatro'] = Dominio.objects.get(pk=4)
	data['dominio_cinco'] = Dominio.objects.get(pk=5)
	data['dominio_seis'] = Dominio.objects.get(pk=6)
	data['dominio_siete'] = Dominio.objects.get(pk=7)
	data['dominio_ocho'] = Dominio.objects.get(pk=8)
	data['dominio_nueve'] = Dominio.objects.get(pk=9)
	data['dominio_diez'] = Dominio.objects.get(pk=10)
	data['dominio_once'] = Dominio.objects.get(pk=11)

	return render(request, template_name, data)