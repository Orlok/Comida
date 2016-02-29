from django.contrib import admin

# Register your models here.
from .models import Platillo

@admin.register(Platillo)
class AdminPlatillo(admin.ModelAdmin):
	list_display = ('nombre','descripcion')