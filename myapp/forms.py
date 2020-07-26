from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Şifrə'
        }
    ))

    class Meta:
        model = User
        fields = ['username']

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'username'
        }
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'password'
        }
    ))
