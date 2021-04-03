from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {'message':'Hello it\'s fine work!' };
    return render(request,'admin/login.html', context=data);
