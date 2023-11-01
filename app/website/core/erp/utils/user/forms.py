from django import forms
from .model import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password1', 'password2','career' ]

class LoginForm(AuthenticationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electrónico'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
    )
    class Meta:
        model = User
        fields = ['email', 'password']