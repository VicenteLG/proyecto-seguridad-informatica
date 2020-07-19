from django.contrib import admin
from .models import Recomendacion

# Register your models here.

@admin.register(Recomendacion)
class RecomendacionAdmin(admin.ModelAdmin):
	list_display = ('recomendacion', 'pk')