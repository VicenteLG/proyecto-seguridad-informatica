from django.urls import path
from Charts import views

urlpatterns = [
	path('', views.encuesta, name='encuesta'),
]