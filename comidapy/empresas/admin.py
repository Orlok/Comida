from django.contrib import admin

# Register your models here.
from .models import Empresa

@admin.register(Empresa)
class AdminEmpresa(admin.ModelAdmin):
	list_display = ('nombre','descripcion', 'createdat', 'createdby')