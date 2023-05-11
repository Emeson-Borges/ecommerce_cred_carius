from django.shortcuts import render
import matplotlib.pyplot as plt
from django.shortcuts import render
from django.views.generic import TemplateView
from app_ecommerce import views

# Create your views here.

def home(request):
  return render(request, 'home/home.html')

def login(request):
  return render(request, 'login/login.html')

def redefinir_senha(request):
  return render(request, 'redefinir_senha/redefinir_senha.html')

def cadastrar_usuario(request):
  return render(request, 'cadastrar_usuario/cadastrar_usuario.html')

#Classe do Modelo do Site
class ModeloView(TemplateView):
    template_name = "modelo_site/modelo_site.html"
    
class HomeView(TemplateView):
  template_name = "home/home.html"