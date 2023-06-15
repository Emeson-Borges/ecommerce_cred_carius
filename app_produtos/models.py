from django.db import models
# Create your models here.

#Tabela de Produtos
class Produtos(models.Model):
  nome      = models.CharField(max_length=100)
  qtdprod   = models.IntegerField(verbose_name="Quantidade de Produtos")
  preco     = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Preço")
  descricao = models.CharField(max_length=255, verbose_name="Descrição")
  
  #Usando a Classe Meta para personalizar o nome da tabela
  class Meta:
    db_table = 'produtos'
  
  def __str__(self) -> str:
    return f"{self.nome} ({self.qtdprod}) {self.preco} {self.descricao}"
  
  
  #