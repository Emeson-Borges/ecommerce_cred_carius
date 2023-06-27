from django.shortcuts import render, redirect
from django.shortcuts import render
from django import http
from django.views.generic import TemplateView
from django.db import models
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import AdminForm,FuncionarioForm

#Importar de onde vem os Models
from app_funcionarios.models import Funcionarios
from app_produtos.models import Produtos
# Create your views here.

def home(request):
  return render(request, 'home/home.html')

def login(request):
  return render(request, 'login/login.html')

def redefinir_senha(request):
  return render(request, 'redefinir_senha/redefinir_senha.html')
#-------------------------------------------------------------------
# Rotas para Cadastrar no Sistema
def cadastrar_usuario(request):
  return render(request, 'cadastrar_usuario/cadastrar_usuario.html')

def cadastrar_funcionario(request):
  return render(request, 'cadastrar_funcionario/cadastrar_funcionario.html')

def cadastrar_produto(request):
  return render(request, 'cadastrar_produto/cadastrar_produto.html')

def cadastrar_vendas(request):
  return render(request, 'cadastrar_vendas/cadastrar_vendas.html')
# -------------------------------------------------------------------

#Rotas para salvar dados no banco 
def cad_produtos(request):
  return render(request, 'cadastrar_produto/cadastrar_produto.html')

# def cad_funcionarios(request):
#   return render(request, 'cadastrar_funcionario/cadastrar_funcionario.html')
# -----------------------------------------------------------------
def vendas(request):
  return render(request, 'vendas/vendas.html')

def relatorios(request):
  return render(request, 'relatorios/relatorios.html')

#Função para listar itens na tela
def lista_produtos(request):
    produtos = Produtos.objects.all()
    return render(request, 'listar_produtos/listar_produtos.html', {'produtos': produtos})

def listar_funcionarios(request):
    funcionarios = Funcionarios.objects.all()
    return render(request, 'listar_funcionarios/listar_funcionario.html', {'funcionarios': funcionarios})

#Classe do Modelo do Site
class ModeloView(TemplateView):
    template_name = "modelo_site/modelo_site.html"
    
class HomeView(TemplateView):
  template_name = "home/home.html"
  
  
  # Perfil do Administrador 
def admin_profile(request):
    # Lógica para recuperar os detalhes do perfil do administrador
    profile_data = {
        'username': request.user.username,
        'email': request.user.email,
        # outros dados relevantes do perfil
    }
    
    return render(request, 'admin/profile.html', {'profile_data': profile_data})

#Criar novo Usuário Administrador 
def create_admin(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            # Cria um novo usuário com as informações fornecidas no formulário
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, email=email, password=password)

            # Redireciona para a página de perfil do administrador recém-criado ou para outra página
            return redirect('admin:admin_profile')
    else:
        form = AdminForm()

    return render(request, 'admin/create_admin.html', {'form': form})
  
# ------  Class para salvar os dados vindo do Front-End  --------

# Salvar na tabela Funcionários
def cad_funcionarios(request):
  if request.method == 'POST':
    form = FuncionarioForm(request.POST)

    if form.is_valid():
      nome        = request.POST['nome']
      email       = request.POST['email']
      cpf         = request.POST['cpf']  
      rg          = request.POST['rg']                
      cidade      = request.POST['cidade']
      rua         = request.POST['rua']
      bairro      = request.POST['bairro']
      dtnasc_func = request.POST['dtnasc_func']
      numero_casa = request.POST['numero_casa']
      contato     = request.POST['contato']
      estadocivil = request.POST['estadocivil']
      sexo        = request.POST['sexo']
      setor       = request.POST.getlist('setor')[0]
      observacao  = request.POST.getlist('observacao')
      estado      = request.POST['estado']
      print(observacao)
      cad_funcionarios = Funcionarios.objects.create(nome=nome,cpf=cpf,rg=rg,cidade=cidade,\
        rua=rua,bairro=bairro,dtnasc_func=dtnasc_func,numero_casa=numero_casa,contato=contato,
        setor=setor,sexo=sexo,estadocivil=estadocivil,observacao = observacao,email=email, estado=estado)
      
      cad_funcionarios.save()
      messages.success(request, 'Funcionário cadastrado com sucesso.')
      #Para depois que as rotas o update e delete tiverem sido feitos
      return redirect('listar_funcionarios')
    else:
       print("CPF: " ,request.POST['cpf'])
       print(form.errors)
       return render(request,'cadastrar_funcionario/cadastrar_funcionario.html',form.errors)

# Salvar na tabela Produtos
def cad_produto(request):
  if request.method == 'POST':
    nome      = request.POST['nome']
    qtdprod   = request.POST['qtdprod']
    preco     = request.POST['preco']
    descricao = request.POST['descricao']
    
    
    cad_produto = Produtos.objects.create(nome=nome,qtdprod=qtdprod,preco=preco,\
      descricao=descricao)
   
    cad_produto.save()
    messages.success(request, 'Produto cadastrado com sucesso.')
    return redirect('cadastrar_produto')
  
  return render(request, 'cadastrar_produto.html')

#Deletar no Banco

def deleta_funcionario(request,pk):
   funcionario=Funcionarios.objects.get(id=pk)
   funcionario.delete()
   messages.success(request,'Funcionário Deletado!')
   return redirect('listar_funcionarios')


#Alterar no banco
def alterar_funcionario(request,pk):
      funcionario = Funcionarios.objects.get(id=pk)
      return render(request, 'alterar_funcionarios/alterar_funcionario.html', {'funcionario':funcionario}) 
   
def upd_funcionario(request):
     if request.method == 'POST':
       funcionario = Funcionarios.objects.get(id=request.POST['id'])

       nome                  = request.POST['nome']
       cpf                   = request.POST['cpf']  
       rg                    = request.POST['rg']                
       cidade                = request.POST['cidade']
       rua                   = request.POST['rua']
       bairro                = request.POST['bairro']
       dtnasc_func           = request.POST['dtnasc_func']
       numero_casa           = request.POST['numero_casa']
       contato               = request.POST['contato']
       sexo                  = request.POST['sexo']
       estadocivil           = request.POST['estadocivil']
       estado                = request.POST['estado']
       observacao            = request.POST['observacao']
       funcionario.nome = nome
       funcionario.cpf = cpf
       funcionario.rg = rg
       funcionario.cidade = cidade
       funcionario.rua = rua
       funcionario.bairro = bairro
       funcionario.dtnasc_func = dtnasc_func
       funcionario.numero_casa = numero_casa
       funcionario.contato = contato
       funcionario.sexo = sexo
       funcionario.estadocivil = estado
       funcionario.observacao = observacao
       funcionario.estado     = estado
       funcionario.estadocivil = estadocivil
       funcionario.save()  
       messages.success(request,'Funcionário Alterado!')
       return redirect('listar_funcionarios')
# Salvar na tabela Vendas

