from django.shortcuts import render, redirect
from django.shortcuts import render
from django import http
from django.views.generic import TemplateView
from django.db import models
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import AdminForm,FuncionarioForm
from django.db.models import Q

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


def filtra_funcionarios(request):
   
   cidade = request.GET.get('cidade')
   sexo   = request.GET.get('sexo')
   print(sexo,'\n')
   setor  = request.GET.get('setor')
   print(setor,'\n')
   if request.method == 'GET':
      funcionarios = Funcionarios.objects

      if cidade != None:
         print('Cidade foi selecionada','\n')
         funcionarios = funcionarios.filter(cidade = cidade)
      if sexo  != None:
         funcionarios = funcionarios.filter(sexo = sexo)
         print('Sexo foi selecionado','\n')
      if setor != None:
         print('Setor foi selecionado','\n')
         funcionarios = funcionarios.filter(setor = setor)

      if not funcionarios.exists():
         funcionarios = Funcionarios.objects.all()
         messages.error(request,'Nenhum funcionário encontrado!')
         return render(request,'listar_funcionarios/listar_funcionario.html',{'funcionarios':funcionarios})
      
      print(funcionarios)
      return render(request,'listar_funcionarios/listar_funcionario.html',{'funcionarios':funcionarios})
def pesquisar_funcionarios(request):
    if request.method == 'GET':
       pesquisa     = request.GET['pesquisa']
       print('Pesquisa:',pesquisa,'\n')
       funcionarios = Funcionarios.objects.filter(Q(nome__contains = pesquisa) | Q(email__contains= pesquisa)| Q(cpf__contains = pesquisa)| 
                                                  Q(rg__contains = pesquisa)|Q(rua__contains=pesquisa)|Q(bairro__contains=pesquisa)|
                                                  Q(numero_casa__contains=pesquisa))
       
       print(funcionarios,'\n')
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
    form   = FuncionarioForm(request.POST)
    estado = request.POST.get('estado')
    cidade = request.POST.get('cidade') 
    if form.is_valid(): 
      
      form.fields['nome'].widget.attrs['class']   = 'form_input'
      form.fields['email'].widget.attrs['class']  = 'form_input'
      form.fields['cpf'].widget.attrs['class']    = 'form_input'
      form.fields['rg'].widget.attrs['class']     = 'form_input'
      form.fields['cidade'].widget.attrs['class'] = 'form_select_option'
      form.fields['rua'].widget.attrs['class']    = 'form_input'
      form.fields['bairro'].widget.attrs['class'] = 'form_input'
      form.fields['dtnasc_func'].widget.attrs['class'] = 'form_input'
      form.fields['numero_casa'].widget.attrs['class'] = 'form_input'
      form.fields['contato'].widget.attrs['class'] = 'form_input'
      form.fields['estadocivil'].widget.attrs['class'] = 'form-input'
      form.fields['sexo'].widget.attrs['class'] = 'form_input'
      form.fields['setor'].widget.attrs['class'] = 'radio-setor'
      form.fields['observacao'].widget.attrs['class'] = 'form_input'
      form.fields['estado'].widget.attrs['class'] = 'form_select_option'

  
      #Checa se já há o mesmo cpf no banco
      if Funcionarios.objects.filter(cpf = form.cleaned_data['cpf']).exists():
         
      
         form.fields['cpf'].widget.attrs['class']    = 'form-error'
         return render(request,'cadastrar_funcionario/cadastrar_funcionario.html',{'mensagem':'Já existe um funcionário com esse CPF',
                                                                                     'form':form,
                                                                                     'cidade':cidade,
                                                                                     'estado':estado})
      #Checa se já há o mesmo rg no banco
      elif Funcionarios.objects.filter(rg = form.cleaned_data['rg']).exists():
         form.fields['rg'].widget.attrs['class']    = 'form-error'
         return render(request,'cadastrar_funcionario/cadastrar_funcionario.html',{'mensagem':'Já existe um funcionário com esse RG',
                                                                                   'form':form,
                                                                                   'cidade':cidade,
                                                                                    'estado':estado})
      #Checa se já há o mesmo email no banco
      elif Funcionarios.objects.filter(email = form.cleaned_data['email']).exists():
         form.fields['email'].widget.attrs['class']    = 'form-error'
         return render(request,'cadastrar_funcionario/cadastrar_funcionario.html',{'mensagem':'Já existe um funcionário com esse Email',
                                                                                   'form':form,
                                                                                   'cidade':cidade,
                                                                                    'estado':estado})
      else:
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
        observacao  = form.cleaned_data['observacao']
        estado      = request.POST['estado']
        print(estado)
        cad_funcionarios = Funcionarios.objects.create(nome=nome,cpf=cpf,rg=rg,cidade=cidade,\
          rua=rua,bairro=bairro,dtnasc_func=dtnasc_func,numero_casa=numero_casa,contato=contato,
          setor=setor,sexo=sexo,estadocivil=estadocivil,observacao = observacao,email=email, estado=estado)
      
      cad_funcionarios.save()
      messages.success(request, 'Funcionário cadastrado com sucesso.')
      #Para depois que as rotas o update e delete tiverem sido feitos
      return redirect('listar_funcionarios')
    else:
       if 'nome' in form.errors:
           form.fields['nome'].widget.attrs['class'] = 'form-error'

       if 'cpf' in form.errors:
            form.fields['cpf'].widget.attrs['class'] = 'form-error'

       if 'email' in form.errors:
            form.fields['email'].widget.attrs['class'] = 'form-error'

       if 'rg' in form.errors:
          form.fields['rg'].widget.attrs['class'] = 'form-error'

       if 'email' in form.errors:
          form.fields['email'].widget.attrs['class'] = 'form-error'
      
       if 'cidade' in form.errors:
          form.fields['cidade'].widget.attrs['class'] = 'form-error'
       
       if 'estado' in form.errors:
          form.fields['estado'].widget.attrs['class'] = 'form-error'

       if 'rua' in form.errors:
          form.fields['rua'].widget.attrs['class'] = 'form-error'

       if 'bairro' in form.errors:
          form.fields['bairro'].widget.attrs['class'] = 'form-error'

       if 'numero_casa' in form.errors:
          form.fields['numero_casa'].widget.attrs['class'] = 'form-error'

       if 'dtnasc_func' in form.errors:
          form.fields['dtnasc_func'].widget.attrs['class'] = 'form-error'

       if 'contato' in form.errors:
          form.fields['contato'].widget.attrs['class'] = 'form-error'
      
       if 'estadocivil' in form.errors:
          form.fields['estadocivil'].widget.attrs['class'] = 'form-error'
      
       if 'sexo' in form.errors:
          form.fields['sexo'].widget.attrs['class'] = 'form-error'
       
       if 'setor' in form.errors:
          form.fields['setor'].widget.attrs['class'] = 'form-error'

       if 'observacao' in form.errors:
          form.fields['observacao'].widget.attrs['class'] = 'form-error'

       
       if form.cleaned_data.get('estado') != '' and form.cleaned_data.get('cidade') != '' :  
          return render(request,'cadastrar_funcionario/cadastrar_funcionario.html',{'form':form,
                                                                                    'cidade':cidade,
                                                                        'estado':estado})
       else:
          return render(request,'cadastrar_funcionario/cadastrar_funcionario.html',{'form':form,
                                                                                    'cidade':cidade,
                                                                        'estado':estado})

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
   messages.warning(request,'Funcionário Deletado!')
   return redirect('listar_funcionarios')


#Alterar no banco
def alterar_funcionario(request,pk):
      funcionario = Funcionarios.objects.get(id=pk)
      return render(request, 'alterar_funcionarios/alterar_funcionario.html', {'funcionario':funcionario}) 
   
def upd_funcionario(request):
     if request.method == 'POST':
       form = FuncionarioForm(request.POST)
       if form.is_valid():
        
        form.fields['nome'].widget.attrs['class']   = 'form_input'
        form.fields['email'].widget.attrs['class']  = 'form_input'
        form.fields['cpf'].widget.attrs['class']    = 'form_input'
        form.fields['rg'].widget.attrs['class']     = 'form_input'
        form.fields['cidade'].widget.attrs['class'] = 'form_select_option'
        form.fields['rua'].widget.attrs['class']    = 'form_input'
        form.fields['bairro'].widget.attrs['class'] = 'form_input'
        form.fields['dtnasc_func'].widget.attrs['class'] = 'form_input'
        form.fields['numero_casa'].widget.attrs['class'] = 'form_input'
        form.fields['contato'].widget.attrs['class'] = 'form_input'
        form.fields['estadocivil'].widget.attrs['class'] = 'form-input'
        form.fields['sexo'].widget.attrs['class'] = 'form_input'
        form.fields['setor'].widget.attrs['class'] = 'form-input'
        form.fields['observacao'].widget.attrs['class'] = 'form_input'
        form.fields['estado'].widget.attrs['class'] = 'form_select_option'
        funcionario = Funcionarios.objects.get(id=request.POST['id'])
        cidade      = form.cleaned_data.get('cidade')
        estado      = form.cleaned_data.get('estado')
        id          = request.POST['id']
        #Checa se já há o mesmo cpf no banco
        if Funcionarios.objects.filter(cpf = form.cleaned_data['cpf']).exclude(id=id).exists():
            form.fields['cpf'].widget.attrs['class']    = 'form-error'
            print("CPF já existe")
            return render(request,'alterar_funcionarios/alterar_funcionario.html',{'mensagem':'Já existe um funcionário com esse CPF',
                                                                                       'form':form,
                                                                                       'id'  : id,
                                                                                       'cidade':cidade,
                                                                                       'estado':estado})
         #Checa se já há o mesmo rg no banco
        elif Funcionarios.objects.filter(rg = form.cleaned_data['rg']).exclude(id=id).exists():
            form.fields['rg'].widget.attrs['class']    = 'form-error'
            print("RG Já existe")
            return render(request,'alterar_funcionarios/alterar_funcionario.html',{'mensagem':'Já existe um funcionário com esse RG',
                                                                                    'form':form,
                                                                                    'id':id,
                                                                                    'cidade':cidade,
                                                                                    'estado':estado})
         #Checa se já há o mesmo email no banco
        elif Funcionarios.objects.filter(email = form.cleaned_data['email']).exclude(id=id).exists():
            form.fields['email'].widget.attrs['class']    = 'form-error'
            print('Email já existe')
            return render(request,'alterar_funcionarios/alterar_funcionario.html',{'mensagem':'Já existe um funcionário com esse Email',
                                                                                    'form':form,
                                                                                    'id'  : id,
                                                                                    'cidade':cidade,
                                                                                       'estado':estado})
        else:
            nome                  = request.POST['nome']
            email                 = request.POST['email']
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
            funcionario.email  = email
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
       else:
        if 'nome' in form.errors:
           form.fields['nome'].widget.attrs['class'] = 'form-error'

        if 'cpf' in form.errors:
              form.fields['cpf'].widget.attrs['class'] = 'form-error'

        if 'email' in form.errors:
              form.fields['email'].widget.attrs['class'] = 'form-error'

        if 'rg' in form.errors:
            form.fields['rg'].widget.attrs['class'] = 'form-error'

        if 'email' in form.errors:
            form.fields['email'].widget.attrs['class'] = 'form-error'
        
        if 'cidade' in form.errors:
            form.fields['cidade'].widget.attrs['class'] = 'form-error'
        
        if 'estado' in form.errors:
            form.fields['estado'].widget.attrs['class'] = 'form-error'

        if 'rua' in form.errors:
            form.fields['rua'].widget.attrs['class'] = 'form-error'

        if 'bairro' in form.errors:
            form.fields['bairro'].widget.attrs['class'] = 'form-error'

        if 'numero_casa' in form.errors:
            form.fields['numero_casa'].widget.attrs['class'] = 'form-error'

        if 'dtnasc_func' in form.errors:
            form.fields['dtnasc_func'].widget.attrs['class'] = 'form-error'

        if 'contato' in form.errors:
            form.fields['contato'].widget.attrs['class'] = 'form-error'
        
        if 'estadocivil' in form.errors:
            form.fields['estadocivil'].widget.attrs['class'] = 'form-error'
        
        if 'sexo' in form.errors:
            form.fields['sexo'].widget.attrs['class'] = 'form-error'
        
        if 'setor' in form.errors:
            form.fields['setor'].widget.attrs['class'] = 'form-error'

       if 'observacao' in form.errors:
          form.fields['observacao'].widget.attrs['class'] = 'form-error'
       id = request.POST['id']
       estado = request.POST['estado']
       cidade = request.POST['cidade']
       print(estado,'\n')
       return render(request,'alterar_funcionarios/alterar_funcionario.html',{'form':form,
                                                                                'id' : id,
                                                                              'estado':estado,
                                                                              'cidade':cidade})
          
# Salvar na tabela Vendas

