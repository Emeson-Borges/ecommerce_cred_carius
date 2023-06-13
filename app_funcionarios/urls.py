from django.urls import path

from .views import FuncionariosCreate
from app_ecommerce import views

urlpatterns = [
    path('cadastrar_funcionario/', FuncionariosCreate.as_view(), name='cadastrar_funcionario'),
]



