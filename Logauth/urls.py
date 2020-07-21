from django.urls import path
from Logauth import views

urlpatterns = [
	path('', views.home, name='home'),
	path('login', views.login, name='login'),
	path('logout', views.logout, name='logout'),
	path('register', views.register, name='register'),
]