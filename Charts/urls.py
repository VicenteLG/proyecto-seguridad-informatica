from django.urls import path
from Charts import views

urlpatterns = [
	path('', views.home, name='chart_home'),
]