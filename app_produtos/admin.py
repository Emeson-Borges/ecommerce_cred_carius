#Importar modulo administrativo
from django.contrib import admin

#Importar classes
from .models import Produtos

# Register your models here.
admin.site.register(Produtos)