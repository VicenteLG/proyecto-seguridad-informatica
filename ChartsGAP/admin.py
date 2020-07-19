from django.contrib import admin
from .models import (
	Respuesta,
	Subcontrol,
	Control,
	Seccion,
	Dominio,
	Evaluacion,
)

# Register your models here.

@admin.register(Respuesta)
class RespuestaAdmin(admin.ModelAdmin):
	pass

@admin.register(Subcontrol)
class SubcontrolAdmin(admin.ModelAdmin):
	list_display = ('nombre_subcontrol', 'pk')

@admin.register(Control)
class ControlAdmin(admin.ModelAdmin):
	list_display = ('nombre_control', 'pk')

@admin.register(Seccion)
class SeccionAdmin(admin.ModelAdmin):
	list_display = ('nombre_seccion', 'pk')

@admin.register(Dominio)
class DominioAdmin(admin.ModelAdmin):
	list_display = ('nombre_dominio', 'pk')

@admin.register(Evaluacion)
class EvaluacionAdmin(admin.ModelAdmin):
	pass