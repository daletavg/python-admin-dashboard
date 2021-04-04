from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import widgets
from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class LoginForm(AuthenticationForm):
    email = forms.EmailInput(
            attrs={'placeholder': "Email", "class": "form-control"})
    password = forms.PasswordInput(
            attrs={'placeholder': "password", "class": "form-control"})

