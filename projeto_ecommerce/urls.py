from django.contrib import admin
from django.urls import path
from app_ecommerce import views
from app_ecommerce.views import ModeloView, HomeView

urlpatterns = [
    
    #rota, view responável, nome de preferência
    path('', ModeloView.as_view(), name='index'),
    path('home/', HomeView.as_view(), name='home'),
    path('login/', views.login, name='login'),
    path('redefinir_senha/', views.redefinir_senha, name='redefinir_senha'),
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario')
]
