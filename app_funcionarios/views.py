from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView

from .models import Funcionarios

from django.urls import reverse_lazy

class FuncionariosCreate(CreateView):
  model = Funcionarios
  fields = ['nome', 'cpf', 'rg', 'rua', 'cidade', 'bairro', 'contato',\
    'dtnasc_func', 'numero_casa', 'estado', 'estado_civil', 'sexo', 'setor', 'observacao', 'email']
  template_name = 'templates/cadastrar_funcionario/cadastrar_funcionario.html'
  
  success_url = reverse_lazy('')

  