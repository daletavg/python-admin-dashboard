from django.shortcuts import render
from django.http import HttpResponse

def show_login(request):
    return render(request,'admin/login.html');
