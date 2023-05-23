#Importar modulo administrativo
from django.contrib import admin

#Importar classes
from .models import produtos

# Register your models here.
admin.site.register(produtos)