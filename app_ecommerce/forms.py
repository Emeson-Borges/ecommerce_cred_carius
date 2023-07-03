from django import forms
estados = [
('acre', 'acre'),
('alagoas', 'alagoas'),
('amapa', 'amapa'),
('amazonas', 'amazonas'),
('bahia', 'bahia'),
('ceara', 'ceara'),
('distrito-federal', 'distrito-federal'),
('espirito-santo', 'espirito-santo'),
('goias', 'goias'),
('maranhao', 'maranhao'),
('mato-grosso', 'mato-grosso'),
('mato-grosso-do-sul', 'mato-grosso-do-sul'),
('minas-gerais', 'minas-gerais'),
('para', 'para'),
('paraiba', 'paraiba'),
('parana', 'parana'),
('pernambuco', 'pernambuco'),
('piaui', 'piaui'),
('rio-de-janeiro', 'rio-de-janeiro'),
('rio-grande-do-norte', 'rio-grande-do-norte'),
('rio-grande-do-sul', 'rio-grande-do-sul'),
('rondonia', 'rondonia'),
('roraima', 'roraima'),
('santa-catarina', 'santa-catarina'),
('sao-paulo', 'sao-paulo'),
('sergipe', 'sergipe'),
('tocantins', 'tocantins')
]

sexo = [("Masculino", "Masculino"),("Feminino","Feminino")]

estado_civil = [('Solteiro','Solteiro(a)'),
('Casado','Casado(a)'),
('Divorciado','Divorcidado(a)'),
('Viúvo','Viúvo(a)')]
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
       sexo             = forms.ChoiceField(label   ="Sexo",widget = forms.RadioSelect,choices = sexo,error_messages={"required":"Sexo não pode ser vazio",
                                                                                                           "invalid":"Sexo inválido"})
       estado           = forms.ChoiceField(label   ="Estado",widget=forms.Select,choices = estados,error_messages={"required":"Estado não pode ser vazio",
                                                                                                           "invalid":"Estado inválido"})
       estadocivil      = forms.ChoiceField(label   = "Estado Civil", widget=forms.Select,choices=estado_civil,error_messages={"required":" Estado Civil não pode ser vazio",
                                                                                                           "invalid":"Estado Civil inválido"})
       observacao       = forms.CharField(label   = "Observação", error_messages={"required":"Observação não pode ser vazio",
                                                                                                           "invalid":"Observação inválida"})
       email            = forms.EmailField(label  ="E-mail",error_messages={"required":"E-mail não pode ser vazio",
                                                                                                           "invalid":"E-mail inválido"})
       setor            = forms.CharField(label   ="Setor", max_length                 = 16,error_messages={"required":"Setor não pode ser vazio",
                                                                                                           "invalid":"Setor inválido"})