from django.shortcuts import render

# Create your views here.

def recomendaciones(request):
	template_name = "recomendaciones.html"
	data = {}

	return render(request, template_name, data)