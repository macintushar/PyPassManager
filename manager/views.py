from django.shortcuts import render, redirect
from .forms import PasswordsForm, NewPasswordsForm, NewUserForm
from .models import Passwords

from hash import HashPassword, UnhashPassword, GeneratePassword

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required

import clipboard

@login_required(login_url='/login/')
def index(request):
    data = Passwords.objects.all().values()
    data = list(data)

    context = {'datas':data, 'name':'Home | PyPassManager'}
    return render(request, "manager/index.html", context= context)

@login_required(login_url='/login/')
def NewPassword(request):
    if request.method == "POST":  
        if len(request.POST.get("password")) == 0: 
            new_password = GeneratePassword()
            new_password = HashPassword(new_password)
            encPassStr = new_password.decode('latin-1')
            encPassStr = str(encPassStr)
            
            app_name = request.POST.get('app_name')
            url = request.POST.get('url')
            username = request.POST.get('username') 
            email = request.POST.get('email')  
            category = request.POST.get('category')     
            password = encPassStr                  

            print("Form saved - Password Generated and Saved")
            try:
                db = Passwords(app_name=app_name,url=url, username=username, email=email,password=password,category=category)
                db.save()

            except:
                print("Unable to save data") 

            return redirect('/')  
        
            if form.is_valid() != True:
                print("Invalid Form - Password Generated")
        
        else:
            print("Password acquired from POST")
            new_password = request.POST.get('password')
            new_password = HashPassword(new_password)
            encPassStr = new_password.decode('latin-1')
            encPassStr = str(encPassStr)
            
            app_name = request.POST.get('app_name')
            url = request.POST.get('url')
            username = request.POST.get('username') 
            email = request.POST.get('email')  
            category = request.POST.get('category')     
            password = encPassStr              

            print(app_name,url,username,email,category,password)      

            try:
                db = Passwords(app_name=app_name,url=url, username=username, email=email,password=password,category=category)
                db.save()

            except:
                print("Unable to save data") 

            return redirect('/')  
        
            if form.is_valid() != True:
                print("Invalid Form - Password Generated")
                
    if request.method == "GET":  
        form = PasswordsForm()
        npform = NewPasswordsForm()
    
    form = PasswordsForm()
    npform = NewPasswordsForm()
    return render(request,'manager/create.html',{'form':form,'npform':npform, 'name':'New Password | PyPassManager'})  

@login_required(login_url='/login/')
def DeletePassword(request,uid):
    delPass = Passwords.objects.all().filter(id=uid)
    delPass.delete()
    return redirect('/')

@login_required(login_url='/login/')
def ViewPassword(request,uid):
    if request.method == "POST":
        if request.POST.get("password") != None:
            new_password = request.POST.get('password')
            new_password = HashPassword(new_password)
            encPassStr = new_password.decode('latin-1')
            encPassStr = str(encPassStr)
            
            app_name = request.POST.get('app_name')
            url = request.POST.get('url')
            username = request.POST.get('username') 
            email = request.POST.get('email')  
            category = request.POST.get('category')     
            password = encPassStr              

            print(app_name,url,username,email,category,password)      

            try:
                db = Passwords.objects.get(id=uid)

                db.app_name = app_name
                db.url = url
                db.username = username
                db.email = email
                db.category = category
                db.password = password
                db.save()
                print(db, "\nUpdated Database")

            except:
                print("Unable to update data") 

            return redirect('/')  
        
            if form.is_valid() != True:
                print("Invalid Form - Password Generated")

    viewPass = Passwords.objects.all().filter(id=uid)
    vals = list(viewPass.values())
    vals = vals[0]

    passKey = vals['password']
    data = vals

    hashedPass = passKey.encode('latin-1')
    actual = UnhashPassword(hashedPass=hashedPass)
    clipboard.copy(actual)

    return render(request,'manager/view-password.html', {'form':data,'password':actual, 'name':'View Password | PyPassManager'})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = auth_login(request, user)
            return redirect('/')
            
    form = AuthenticationForm()
    return render(request,'manager/login.html',{'form':form})

def Logout(request):
    logout(request)
    return redirect("/login/")

def create_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            form = auth_login(request, user)
            return redirect("/")
    form = NewUserForm()
    return render (request=request, template_name="manager/register.html", context={"register_form":form})