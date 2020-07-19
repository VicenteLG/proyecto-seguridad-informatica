from django.urls import path
from ChartsGAP import views

urlpatterns = [
	path('home', views.home, name='home'),
	path('analisis', views.analisis, name='analisis'),
	path('analisis/dominio_uno/<int:pk>', views.analisis_uno, name='analisis_uno'),
	path('analisis/dominio_dos/<int:pk>', views.analisis_dos, name='analisis_dos'),
	path('analisis/dominio_tres/<int:pk>', views.analisis_tres, name='analisis_tres'),
	path('analisis/dominio_cuatro/<int:pk>', views.analisis_cuatro, name='analisis_cuatro'),
	path('analisis/dominio_cinco/<int:pk>', views.analisis_cinco, name='analisis_cinco'),
	path('analisis/dominio_seis/<int:pk>', views.analisis_seis, name='analisis_seis'),
	path('analisis/dominio_siete/<int:pk>', views.analisis_siete, name='analisis_siete'),
	path('analisis/dominio_ocho/<int:pk>', views.analisis_ocho, name='analisis_ocho'),
	path('analisis/dominio_nueve/<int:pk>', views.analisis_nueve, name='analisis_nueve'),
	path('analisis/dominio_diez/<int:pk>', views.analisis_diez, name='analisis_diez'),
	path('analisis/dominio_once/<int:pk>', views.analisis_once, name='analisis_once'),
]