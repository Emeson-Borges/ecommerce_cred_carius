from django.urls import path

from .views import ProdutosCreate


urlpatterns = [
    path('cadastrar_produto/', ProdutosCreate.as_view(), name='cadastrar_produto')
]