from django.shortcuts import render
from ChartsGAP.models import Evaluacion


# Create your views here.

def encuesta(request):
	template_name = 'encuesta.html'
	data = {}

	data['evaluacion'] = Evaluacion.objects.all()

	return render(request, template_name, data)