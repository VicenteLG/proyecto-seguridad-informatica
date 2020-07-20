from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CARGO = (
	('XX', 'INSERTAR CARGO'),
	('XX', 'INSERTAR CARGO'),
)

DEPARTAMENTO = (
	('XX', 'INSERTAR DEPARTAMENTO'),
	('XX', 'INSERTAR DEPARTAMENTO'),
)

SUCURSAL = (
	('SA', 'Santiago'),
	('PR', 'Providencia'),
)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	primer_nombre = models.CharField(max_length=25)
	segundo_nombre = models.CharField(max_length=25)
	apellido_paterno = models.CharField(max_length=25)
	apellido_materno = models.CharField(max_length=25)
	age = models.PositiveIntegerField(default=1)
	email = models.EmailField()
	rut = models.CharField(max_length=12)
	cargo = models.CharField(choices=CARGO, max_length=2)
	departamento = models.CharField(choices=DEPARTAMENTO, max_length=2)
	sucursal = models.CharField(choices=SUCURSAL, max_length=2)
	dominio_uno = models.BooleanField(default=False)
	dominio_dos = models.BooleanField(default=False)
	dominio_tres = models.BooleanField(default=False)
	dominio_cuatro = models.BooleanField(default=False)
	dominio_cinco = models.BooleanField(default=False)
	dominio_seis = models.BooleanField(default=False)
	dominio_siete = models.BooleanField(default=False)
	dominio_ocho = models.BooleanField(default=False)
	dominio_nueve = models.BooleanField(default=False)
	dominio_diez = models.BooleanField(default=False)
	dominio_once = models.BooleanField(default=False)