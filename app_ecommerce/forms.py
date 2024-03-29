from django import forms
estados = [
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
]

sexo = [("M", "Masculino"),("F","Feminino")]

estado_civil = [('Solteiro','Solteiro(a)'),
('Casado','Casado(a)'),
('Divorciado','Divorcidado(a)'),
('Viúvo','Viúvo(a)')]

setor = [
      ('Vendas','Vendas'),
      ('Entrega', 'Entrega'),
      ('Financeiro','Financeiro'),
      ('Cobrador','Cobrador')
]
class AdminForm(forms.Form):
    username = forms.CharField(label='Nome de usuário')
    email    = forms.EmailField(label='E-mail')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

class FuncionarioForm(forms.Form):
       nome             = forms.CharField(label   = "Nome", max_length                = 100,error_messages={
             "required": "Nome não pode ser vazio",
             "invalid" : "Nome inválido"},
             widget = forms.TextInput(attrs={'placeholder':'Nome do Funcionário','class':'form-input'}))
       cpf              = forms.CharField(label   = "CPF", widget= forms.TextInput(attrs={'id':'cpf','placeholder':'CPF do Funcionário','class':'form-input'}),max_length                 = 14,error_messages={"required":"CPF não pode ser vazio",
                                                                                                           "invalid" : "CPF Inválido"})
       rg               = forms.CharField(label   = "RG", max_length                  = 12,error_messages={"required":"RG não pode ser vazio",
                                                                                                           "invalid":"RG Inválido"},
                                                                                            widget=forms.TextInput(attrs={'id':'rg','placeholder':'RG do Funcionário'}))               
       cidade           = forms.CharField(label   = "Cidade", widget= forms.TextInput(attrs={'id':'cidade',
                                                                                             'class':'form-input',
                                                                                             'placeholder':'Cidade do Funcionário',
                                                                                             }),max_length              = 50,error_messages={"required":"Cidade não pode ser vazio",
                                                                                                           "invalid":"Cidade Inválida"})
       rua              = forms.CharField(label   = "Rua", widget= forms.TextInput(attrs={'id':'rua',
                                                                                             'class':'form-input',
                                                                                             'placeholder':'Rua do Funcionário',
                                                                                             }),max_length                 = 50,error_messages={"required":"Rua não pode ser vazio",
                                                                                                           "invalid":"Rua inválida"})
       bairro           = forms.CharField(label   = "Bairro" ,widget= forms.TextInput(attrs={'id':'bairro',
                                                                                             'class':'form-input',
                                                                                             'placeholder':'Bairro do Funcionário',
                                                                                             }),max_length              = 50,error_messages={"required":"Bairro não pode ser vazio",
                                                                                                           "invalid":"Bairro"})
       dtnasc_func      = forms.CharField(label   = "Data de Nascimento",widget = forms.TextInput(attrs={'id':'dtnasc_func',
                                                                                                         'class':'form-input',
                                                                                                          'placeholder':'Bairro do Funcionário'}),max_length  = 10,error_messages={"required":"Data de nascimento não pode ser vazia",
                                                                                                           "invalid":"Data de nascimento inválida"})
       
       numero_casa      = forms.IntegerField(label="Numero da Casa", widget = forms.TextInput(attrs = {'id':'numero_casa',
                                                                                                       'class':'form-input',
                                                                                                       'type' : 'number',  
                                                                                                       'placeholder':'Número da Casa do Funcionário'
                                                                                                      }),error_messages={"required":"Numero da casa não pode ser vazio",
                                                                                                           "invalid":"Numero da casa inválido"}) 
       
       contato          = forms.CharField(label   = "Contato" , max_length            = 15,widget = forms.TextInput(attrs = {'id':'contato',
                                                                                                       'class':'form-input',   
                                                                                                       'placeholder':'Número da Casa do Funcionário'
                                                                                                      }),error_messages={"required":"Contato não pode ser vazio",
                                                                                                           "invalid":"COntato inválido"})
       sexo             = forms.ChoiceField(label   ="Sexo",widget = forms.RadioSelect(attrs={'class':'form-input'}),choices = sexo,error_messages={"required":"Sexo não pode ser vazio",
                                                                                                           "invalid":"Sexo inválido"})
       estado           = forms.ChoiceField(label   ="Estado",widget=forms.Select(attrs={'id':'estado','class':'form-input'}),choices = estados,error_messages={"required":"Estado não pode ser vazio",
                                                                                                           "invalid":"Estado inválido"})
       estadocivil      = forms.ChoiceField(label   = "Estado Civil", widget=forms.Select(attrs={'class':'form-input'}),choices=estado_civil,error_messages={"required":" Estado Civil não pode ser vazio",
                                                                                                           "invalid":"Estado Civil inválido"})
       observacao       = forms.CharField(label   = "Observação", widget = forms.Textarea(attrs = {"rows":"3","cols":"30",'class':'form-input'}),error_messages={"required":"Observação não pode ser vazio",
                                                                                                           "invalid":"Observação inválida"})
       email            = forms.EmailField(label  ="E-mail",widget=forms.EmailInput(attrs={'class':'form-input','placeholder':'E-mail do Funcionário'}),error_messages={"required":"E-mail não pode ser vazio",
                                                                                                           "invalid":"E-mail inválido"})
       setor            = forms.ChoiceField(label   ="Setor", widget=forms.RadioSelect(attrs={'class':'form-input'}),choices = setor,error_messages={"required":"Setor não pode ser vazio",
                                                                                                           "invalid":"Setor inválido"})