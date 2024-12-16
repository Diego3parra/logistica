from django import forms
from django.contrib.auth.forms import UserCreationForm
from  authtools.models import User

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'password1', 'password2']

class InicioSesionForm(forms.Form):
    email = forms.EmailField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)