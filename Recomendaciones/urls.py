from django.urls import path
from Recomendaciones import views

urlpatterns = [
	path('', views.recomendaciones, name='recomendaciones'),
]