from django import forms

class AdminForm(forms.Form):
    username = forms.CharField(label='Nome de usuário')
    email    = forms.EmailField(label='E-mail')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

class FuncionarioForm(forms.Form):
       nome             = forms.CharField(label = "Nome", max_length                = 100)
       cpf              = forms.CharField(label = "CPF", max_length                 = 11)
       rg               = forms.CharField(label = "RG", max_length                  = 11)               
       cidade           = forms.CharField(label = "Cidade", max_length              = 50)
       rua              = forms.CharField(label = "Rua", max_length                 = 50)
       bairro           = forms.CharField(label = "Bairro" ,max_length               = 50)
       dtnasc_func      = forms.CharField(label = "Data de Nascimento", max_length  = 10)
       numero_casa      = forms.IntegerField(label="Numero da Casa") 
       contato          = forms.CharField(label = "Contato" , max_length            = 15)
       sexo             = forms.CharField(label ="Sexo", max_length                 = 9)
       estado           = forms.CharField(label ="Estado", max_length               = 50)
       estadocivil      = forms.CharField(label = "Estado Civil", max_length        = 15)
       observacao       = forms.CharField(label = "Observação")
       email            = forms.EmailField(label="E-mail")