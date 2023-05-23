from django import forms

class AdminForm(forms.Form):
    username = forms.CharField(label='Nome de usuário')
    email = forms.EmailField(label='E-mail')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
