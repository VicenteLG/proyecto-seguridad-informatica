from django.shortcuts import render
from ChartsGAP.models import Evaluacion

# Create your views here.

def home(request):
	template_name = 'charts_home.html'
	data = {}

	data['evaluacion'] = Evaluacion.objects.all()

	return render(request, template_name, data)