from django.shortcuts import render, redirect
from ChartsGAP.models import (
	Dominio,
	Recomendacion
)

# Create your views here.

def recomendaciones(request):
	template_name = "recomendaciones.html"
	data = {}
	data['dominios'] = Dominio.objects.all()
	data['recomendaciones'] = Recomendacion.objects.all()
	return render(request, template_name, data)




