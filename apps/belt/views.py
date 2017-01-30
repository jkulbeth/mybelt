from django.shortcuts import render, redirect
from  ..login.models import User

def index(request):
    user = User.objects.get(id=request.session['logged_in_as'])
    
    context = {
        'users' : user
    }
    
    return render(request, "belt/index.html",context)

def log_out(request):
    
    request.session.pop('logged_in_as')

    return redirect( "/")