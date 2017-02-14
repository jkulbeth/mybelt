from django.shortcuts import render, redirect
from  ..login.models import *

def index(request):
    user = User.objects.get(id=request.session['logged_in_as'])
    you = Item.objects.filter(users=user) 
    them = Item.objects.exclude(users=user)
    
    context = {
			'users': User.objects.get(id=request.session['logged_in_as']),
			'yours': you,
			'theres': them,
    }
    
 
    return render(request, "belt/index.html", context)

def log_out(request):
    
    request.session.pop('logged_in_as')

    return redirect( "/")

def add(request):
    return render(request,'belt/item_create.html')

def item_create(request):
    create = Item.objects.item_create(request)
    
    if not create:
        return render(request,"/")
    else:
        return redirect ('/dashboard')
    
def item_remove(request, id):
    item = Item.objects.get(id=id)
    user = User.objects.get(id=request.session['logged_in_as'])
    item.users.remove(user)
    return redirect("/dashboard")

def item_delete(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return redirect("/dashboard")

def item_show(request,id):
    wish = Item.objects.get(id=id)
    user = User.objects.all()
    context ={
        
        "wishes" : wish,
        'users': user
    }
  
    return render(request,'belt/item_show.html', context)

def item_added(request,id):
    wish = Item.objects.get(id=id)
    user = User.objects.get(id=request.session['logged_in_as'])
    wish.users.add(user)
    wish.save()
    return redirect('/dashboard')
    

