from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from app_ecommerce import views
from app_ecommerce.views import ModeloView, HomeView
# from .views import lista_produtos

urlpatterns = [
    
    #rota, view responável, nome de preferência
    #Rota do Rest Framework
    path('api-auth/', include('rest_framework.urls')),
    
    path('perfil/', views.admin_profile, name='admin_profile'),
    path('novo_admin/', views.create_admin, name='create_admin'),
    path('admin/', admin.site.urls),
    path('home/', ModeloView.as_view(), name='index'),
    path('', HomeView.as_view(), name='home'),
    path('login/', views.login, name='login'),
    path('redefinir_senha/', views.redefinir_senha, name='redefinir_senha'),
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('cadastrar_funcionario/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('cadastrar_produto/', views.cadastrar_produto, name='cadastrar_produto'),
    path('vendas', views.vendas, name='Vendas'),
    path('', include('app_funcionarios.urls')),
    path('relatorios/', views.relatorios, name='relatorios' ),

    
    
    #Rotas para listar itens
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    # path('vendas/', views.lista_vendas, name='lista_vendas'),
    path('funcionarios/', views.listar_funcionarios, name='listar_funcionarios'),
    
    
    
    #Rotas que salvam dados na tabela
    path('cad_funcionarios/', views.cad_funcionarios, name='cad_funcionarios'),
    path('cad_produtos/', views.cad_produtos, name='cad_produtos'),
    path('cadastrar_vendas/', views.cadastrar_vendas, name='cadastrar_vendas'),
    
    #Rotas que alteram os dados na tabela
    path('alterar_funcionario/<int:pk>/', views.alterar_funcionario,name='alterar_funcionario'),
    path('upd_funcionario/', views.upd_funcionario,name='upd_funcionario'),
    
    #Rotas que deletam dados
    path('deleta_funcionario/<int:pk>', views.deleta_funcionario,name='deleta_funcionario')
    
]


urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]