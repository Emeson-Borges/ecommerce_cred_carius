from django.urls import path

from .views import FuncionariosCreate


urlpatterns = [
    path('cadastrar_funcionario/', FuncionariosCreate.as_view(), name='cadastrar_funcionario')
]



