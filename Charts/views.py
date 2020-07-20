from django.shortcuts import render

# Create your views here.

def home(request):
	template_name = 'charts_home.html'
	data = {}

	return render(request, template_name, data)