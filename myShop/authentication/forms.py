from .models import User
from django.forms import ModelForm, TextInput, PasswordInput


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'phone', 'password']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Иванов Сергей Иванович'
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер телефона',
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль',
                'type': 'password'
            })
        }


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['phone', 'password']

        widgets = {
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер телефона',
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль',
                'type': 'password'
            })
        }
