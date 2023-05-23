from django.db import models

# Create your models here.
#Tabela de Vendas
class vendas(models.Model):
  dtvenda    = models.DateField(max_length=8)
  id_cliente = models.IntegerField(verbose_name="Quantidade de Produtos")
  id_prod    = models.IntegerField(verbose_name="Preço")
  id_func    = models.IntegerField(verbose_name="Descrição")
  
  #Usando a Classe Meta para personalizar o nome da tabela
  class Meta:
    db_table = 'vendas'
  
  def __str__(self) -> str:
    return f"{self.dtvenda} ({self.id_cliente}) {self.id_prod} {self.id_func}"