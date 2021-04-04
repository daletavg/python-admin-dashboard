from django.shortcuts import render
from .forms import LoginForm

from django.http import HttpResponse

def login(request):
    loginForm = LoginForm()
    return render(request, 'admin/login.html', context={'form':loginForm});
