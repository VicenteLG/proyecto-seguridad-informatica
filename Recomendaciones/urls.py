from django.urls import path
from Recomendaciones import views

urlpatterns = [
	path('recomendaciones', views.recomendaciones, name='recomendaciones'),
]