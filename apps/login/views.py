from django.shortcuts import render, redirect, HttpResponse
from .models import *

def index(request):
    return render(request,'login/index.html')


def register(request):
    val_reg = User.objects.register(request)
    if val_reg:
        return redirect ('/dashboard')
    else:
        return redirect('/')


def login(request):
    val_log = User.objects.login(request)
    
    if val_log:
            
        return redirect ('/dashboard')
    else:
        
        return redirect('/')

