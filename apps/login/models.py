from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import bcrypt
import re


class UserManager(models.Manager):
    def register(self,request):
        # make sure form is validated
        is_valid = True
        
        if len(request.POST['first_name']) == 0:
            messages.error(request, "First name space cannot be empty*");
            is_valid = False
            
        if len(request.POST['last_name']) == 0:
            messages.error(request, 'Last name space cannot be empty*');
            is_valid = False
            
        email_match = User.objects.filter(email=request.POST['email'])
        
        addressToVerify = request.POST['email']
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)
        
        if match == None:
            messages.error(request, "Email is invalid or space is empty**")
            is_valid = False
        
        if len(email_match) > 0:
            messages.error(request, "That email is already in use**")
            is_valid = False
            
        #if len(request.POST['email']) == 0:
        #    messages.error(request, 'email space cannot be empty*');
        #    is_valid = False
            
        if len(request.POST['password']) == 0:
            messages.error(request, 'password space cannot be empty*');
            is_valid = False
            
        if request.POST['password'] != request.POST['password_confirm']:
            messages.error(request, "passwords do not match*");
            is_valid = False
       
        if not is_valid:
            return False        
        
        
        
        hashpw = bcrypt.hashpw(request.POST['password'].encode('utf-8'), bcrypt.gensalt())
        
        #save the new user
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = hashpw
        )
        user.save();
        
        request.session['logged_in_as'] = user.id
        
        return True
    
    def login(self, request):
        #who is logging in
        users = User.objects.filter(email=request.POST['email'])
        #does this person exist
        if len(users) == 0:
            messages.error(request, 'Invalid Email*')
            return False
        
        user = users[0]
        
        test_hash = bcrypt.hashpw(request.POST['password'].encode('utf-8'), user.password.encode('utf-8'))
        
        if test_hash != user.password:
            messages.error(request, "Incorrect Password*")
            return False
        
        request.session['logged_in_as'] = user.id
        
        return True
        
class ItemManager(models.Manager):
    def item_create(self, request):
        
        is_valid = True
        
        if len(request.POST['item_create']) == 0:
            messages.error(request, " Space cannot be empty*");
            is_valid = False
            
        if len(request.POST['item_create']) < 4:
            messages.error(request, "*Item cannot be less than 3 characters long*");
            is_valid = False
            
        if not is_valid:
            return False
       
        
        
        user = User.objects.get(id=request.session['logged_in_as'])
        
        create = Item.objects.create(item=request.POST['item_create'],wished=user) 
 			 	
        create.users.add(user)
        create.save()
        return True

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()
    #having log_in issues when I try to add these to the tables..leaving them out, for now
    #created_at = models.DateTimeField(auto_now_add = True)
    #updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    
class Item(models.Model):
    users = models.ManyToManyField(User, related_name='wished_for')
    
    wished = models.ForeignKey(User)
    
    item = models.CharField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    updated_at = models.DateTimeField(auto_now = True)
    
    objects = ItemManager()
    
    
        
    