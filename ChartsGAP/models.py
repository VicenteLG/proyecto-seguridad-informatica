from django.db import models
from Logauth.models import Profile
from Recomendaciones.models import Recomendacion

# Create your models here.

class Respuesta(models.Model):
	respuesta = models.BooleanField(default=False)
	autor = models.ForeignKey(Profile, on_delete=models.CASCADE)

class Subcontrol(models.Model):
	nombre_subcontrol = models.TextField(blank=True)
	total = models.BooleanField(default=False)
	respuesta = models.ManyToManyField(Respuesta, null=True, blank=True)

class Control(models.Model):
	nombre_control = models.CharField(max_length=100)
	porcentaje_cumplimiento = models.PositiveIntegerField(default=0)
	porcentaje_no_cumplimiento = models.PositiveIntegerField(default=0)
	subcontrol = models.ManyToManyField(Subcontrol, null=True, blank=True)

class Seccion(models.Model):
	nombre_seccion = models.CharField(max_length=75)
	porcentaje_cumplimiento = models.PositiveIntegerField(default=0)
	porcentaje_no_cumplimiento = models.PositiveIntegerField(default=0)
	control = models.ManyToManyField(Control, null=True, blank=True)

class Encuestados(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	fecha_encuesta = models.DateTimeField()

class Dominio(models.Model):
	nombre_dominio = models.CharField(max_length=75)
	porcentaje_cumplimiento = models.PositiveIntegerField(default=0)
	porcentaje_no_cumplimiento = models.PositiveIntegerField(default=0)
	seccion = models.ManyToManyField(Seccion, null=True, blank=True)
	recomendacion = models.ManyToManyField(Recomendacion, null=True, blank=True)
	responsable = models.ForeignKey(Profile, on_delete=models.CASCADE)
	encuestados = models.ManyToManyField(Encuestados, null=True, blank=True)

class Evaluacion(models.Model):
	porcentaje_cumplimiento = models.PositiveIntegerField(default=0)
	porcentaje_no_cumplimiento = models.PositiveIntegerField(default=0)
	dominio = models.ManyToManyField(Dominio, null=True, blank=True)