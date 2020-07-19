from django.db import models
from Logauth.models import Profile

TIPO = (
	('25', '25%'),
	('50', '50%'),
	('75', '75%'),
)

# Create your models here.

class Recomendacion(models.Model):
	recomendacion = models.TextField(blank=True)
	autor = models.ForeignKey(Profile, on_delete=models.CASCADE)
	fecha_recomendacion = models.DateTimeField()
	tipo_recomendacion = models.CharField(choices=TIPO, max_length=2)