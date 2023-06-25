from django.db import models

# Create your models here.
class Funcionarios(models.Model):
  nome             = models.CharField(max_length=100, verbose_name='Nome do Funcionário',null=False)
  email            = models.EmailField(max_length=100,verbose_name='Email',null=False)
  contato          = models.CharField(max_length=15, verbose_name='Número de Telefone',null=False)
  cpf              = models.CharField(max_length=11, verbose_name='CPF do Funcionário', null=False)
  rg               = models.CharField(max_length=11, verbose_name='RG do Funcionário', null = False)
  cidade           = models.CharField(max_length=50, verbose_name='Cidade', null = False)
  rua              = models.CharField(max_length=50, verbose_name='Rua', null = False)
  bairro           = models.CharField(max_length=50, verbose_name='Bairro', null = False)
  numero_casa      = models.IntegerField(verbose_name='Número da casa', null = False)
  dtnasc_func      = models.CharField(max_length=10, verbose_name='Data de Nascimento do Funcionário', null = False)
  sexo             = models.CharField(max_length=9, verbose_name="Sexo do funcionário", null = False)
  estadocivil      = models.CharField(max_length=15, verbose_name="Estado civil", null = False)
  setor            = models.CharField(max_length=16, verbose_name="Setor", null = False)
  observacao       = models.TextField(verbose_name="Observação"'', null = False) 
  estado           = models.CharField(max_length=50, verbose_name="Estado de Origem", null=False) 
  
  class Meta:
    db_table = 'funcionarios'
    
  def __str__(self) -> str:
    return f"{self.nome} {self.contato} {self.cpf} {self.rg} {self.rua} {self.bairro} {self.numero_casa} {self.dtnasc_func} {self.cidade}"
  