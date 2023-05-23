from django.db import models

# Create your models here.
class clientes(models.Model):
  nome     = models.CharField(max_length=100, verbose_name='Nome do Cliente')
  cpf      = models.CharField(max_length=11, verbose_name='CPF do Cliente')
  rg       = models.CharField(max_length=11, verbose_name='RG do Cliente') 
  endereco = models.CharField(max_length=50, verbose_name='Endereço do Cliente')
  dtnasce  = models.DateField(max_length=8, verbose_name='Data de Nascimento do Cliente')
  contato  = models.CharField(max_length=15, verbose_name='Contato do Cliente')

  class Meta:
        db_table = 'clientes'
  
  def __str__(self) -> str:
    return f"{self.nome} ({self.cpf}) {self.rg} {self.cpf} {self.rg} {self.endereco} {self.dtnasce} {self.contato}"
  