from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView

from .models import funcionarios

from django.urls import reverse_lazy

class FuncionariosCreate(CreateView):
  model = funcionarios
  fields = ['nome', 'cpf', 'rg', 'rua', 'cidade', 'bairro', 'contato',\
    'dtnasc_func', 'numero_casa']
  template_name = 'templates/cadastrar_funcionario/cadastrar_funcionario.html'
  success_url = reverse_lazy('')