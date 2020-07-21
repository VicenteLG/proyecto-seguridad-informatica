from django.urls import path
from ChartsGAP import views

urlpatterns = [
	path('', views.analisis, name='analisis'),
	path('dominio_uno/<int:pk>', views.analisis_uno, name='analisis_uno'),
	path('dominio_dos/<int:pk>', views.analisis_dos, name='analisis_dos'),
	path('dominio_tres/<int:pk>', views.analisis_tres, name='analisis_tres'),
	path('dominio_cuatro/<int:pk>', views.analisis_cuatro, name='analisis_cuatro'),
	path('dominio_cinco/<int:pk>', views.analisis_cinco, name='analisis_cinco'),
	path('dominio_seis/<int:pk>', views.analisis_seis, name='analisis_seis'),
	path('dominio_siete/<int:pk>', views.analisis_siete, name='analisis_siete'),
	path('dominio_ocho/<int:pk>', views.analisis_ocho, name='analisis_ocho'),
	path('dominio_nueve/<int:pk>', views.analisis_nueve, name='analisis_nueve'),
	path('dominio_diez/<int:pk>', views.analisis_diez, name='analisis_diez'),
	path('dominio_once/<int:pk>', views.analisis_once, name='analisis_once'),
]