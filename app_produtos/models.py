from django.db import models
# Create your models here.

class nomeproduto(models.Model):
  nome    = models.CharField(max_length=100)
  qtdprod = models.IntegerField(max_length=255, verbose_name="Quantidade de Produtos")
  preco   = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Preço")
  descricao = models.CharField(max_length=255, verbose_name="Descrição")
  
