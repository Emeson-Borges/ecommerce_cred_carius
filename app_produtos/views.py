from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Produtos
from django.urls import reverse_lazy

# Create your views here.

class ProdutosCreate(CreateView):
  model = Produtos
  fields = ['nome','qtdprod','preco','descricao']
  template_name = 'templates/cadastrar_produto/cadastrar_produto.html'
  success_url = reverse_lazy('')