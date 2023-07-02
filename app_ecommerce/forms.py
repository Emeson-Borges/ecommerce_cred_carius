from django import forms

class AdminForm(forms.Form):
    username = forms.CharField(label='Nome de usuário')
    email    = forms.EmailField(label='E-mail')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

class FuncionarioForm(forms.Form):
       nome             = forms.CharField(label   = "Nome", max_length                = 100,error_messages={
             "required": "Nome não pode ser vazio",
             "invalid" : "Nome inválido"})
       cpf              = forms.CharField(label   = "CPF", max_length                 = 11,error_messages={"required":"CPF não pode ser vazio",
                                                                                                           "invalid" : "CPF Inválido"})
       rg               = forms.CharField(label   = "RG", max_length                  = 11,error_messages={"required":"RG não pode ser vazio",
                                                                                                           "invalid":"RG Inválido"})               
       cidade           = forms.CharField(label   = "Cidade", max_length              = 50,error_messages={"required":"Cidade não pode ser vazio",
                                                                                                           "invalid":"Cidade Inválida"})
       rua              = forms.CharField(label   = "Rua", max_length                 = 50,error_messages={"required":"Rua não pode ser vazio",
                                                                                                           "invalid":"Rua inválida"})
       bairro           = forms.CharField(label   = "Bairro" ,max_length              = 50,error_messages={"required":"Bairro não pode ser vazio",
                                                                                                           "invalid":"Bairro"})
       dtnasc_func      = forms.CharField(label   = "Data de Nascimento", max_length  = 10,error_messages={"required":"Data de nascimento não pode ser vazia",
                                                                                                           "invalid":"Data de nascimento inválida"})
       numero_casa      = forms.IntegerField(label="Numero da Casa", error_messages={"required":"Numero da casa não pode ser vazio",
                                                                                                           "invalid":"Numero da casa inválido"}) 
       contato          = forms.CharField(label   = "Contato" , max_length            = 15,error_messages={"required":"Contato não pode ser vazio",
                                                                                                           "invalid":"COntato inválido"})
       sexo             = forms.ChoiceField(label   ="Sexo",widget = forms.RadioSelect,choices = [("1", "Masculino"),("2","Feminino")],error_messages={"required":"Sexo não pode ser vazio",
                                                                                                           "invalid":"Sexo inválido"})
       estado           = forms.ChoiceField(label   ="Estado",widget=forms.Select,choices =[(1, "Acre"),
                                                                                            (2, "Alagoas"),
                                                                                            (3, "Amapá"),
                                                                                            (4, "Amazonas"),
                                                                                            (5, "Bahia"),
                                                                                            (6, "Ceará"),
                                                                                            (7, "Distrito Federal"),
                                                                                            (8, "Espírito Santo"),
                                                                                            (9, "Goiás"),
                                                                                            (10, "Maranhão"),
                                                                                            (11, "Mato Grosso"),
                                                                                            (12, "Mato Grosso do Sul"),
                                                                                            (13, "Minas Gerais"),
                                                                                            (14, "Pará"),
                                                                                            (15, "Paraíba"),
                                                                                            (16, "Paraná"),
                                                                                            (17, "Pernambuco"),
                                                                                            (18, "Piauí"),
                                                                                            (19, "Rio de Janeiro"),
                                                                                            (20, "Rio Grande do Norte"),
                                                                                            (21, "Rio Grande do Sul"),
                                                                                            (22, "Rondônia"),
                                                                                            (23, "Roraima"),
                                                                                            (24, "Santa Catarina"),
                                                                                            (25, "São Paulo"),
                                                                                            (26, "Sergipe"),
                                                                                            (27, "Tocantins")],error_messages={"required":"Estado não pode ser vazio",
                                                                                                           "invalid":"Estado inválido"})
       estadocivil      = forms.ChoiceField(label   = "Estado Civil", widget=forms.Select,choices=[('1','Solteiro(a)'),
                                                                                                   ('2','Casado(a)'),
                                                                                                   ('3','Divorcidado(a)'),
                                                                                                   ('4','Viúvo(a)')],error_messages={"required":" Estado Civil não pode ser vazio",
                                                                                                           "invalid":"Estado Civil inválido"})
       observacao       = forms.CharField(label   = "Observação", error_messages={"required":"Observação não pode ser vazio",
                                                                                                           "invalid":"Observação inválida"})
       email            = forms.EmailField(label  ="E-mail",error_messages={"required":"E-mail não pode ser vazio",
                                                                                                           "invalid":"E-mail inválido"})
       setor            = forms.CharField(label   ="Setor", max_length                 = 16,error_messages={"required":"Setor não pode ser vazio",
                                                                                                           "invalid":"Setor inválido"})