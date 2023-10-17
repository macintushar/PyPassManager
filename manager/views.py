from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from .forms import NewUserForm
from hasher import GeneratePassword, HashPassword, UnhashPassword
from .models import Passwords


# Create your views here.
@login_required(login_url='/login/')    
def index(request):
    user = request.user
    data = Passwords.objects.all().values().filter(user= user)
    data = list(data)
    for i in data:
        pwd = i["password"]
        encoded_pwd = pwd.encode('latin-1')
        password = UnhashPassword(encoded_pwd)
        i["password"] = password


    context = {'datas':data, 'name':'Home | PyPassManager'}
    return render(request, "index.html", context= context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = auth_login(request, user)
            return redirect('/')
        else:
            messages.add_message(request, messages.WARNING, 'Invalid Username or Password')
            form = AuthenticationForm()
            return render(request,'login.html',{'form':form})

            
    form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

@login_required(login_url='/login/')
def NewPassword(request):
        if request.method == "POST":  
            if len(request.POST.get("password")) == 0: 
                new_password = GeneratePassword()
                new_password = HashPassword(new_password)
                encPassStr = new_password.decode('latin-1')
                encPassStr = str(encPassStr)
                
                user = request.user
                app_name = request.POST.get('app_name')
                url = request.POST.get('url')
                username = request.POST.get('username') 
                email = request.POST.get('email')  
                category = request.POST.get('category')     
                password = encPassStr                  

                #print("Form saved - Password Generated and Saved")
                try:
                    db = Passwords(user=user, app_name=app_name,url=url, username=username, email=email,password=password,category=category)
                    db.save()

                except:
                    print("Unable to save data") 

                return redirect('/')  
            
            else:
                #print("Password acquired from POST")
                new_password = request.POST.get('password')
                new_password = HashPassword(new_password)
                encPassStr = new_password.decode('latin-1')
                encPassStr = str(encPassStr)
                
                user = request.user
                app_name = request.POST.get('app_name')
                url = request.POST.get('url')
                username = request.POST.get('username') 
                email = request.POST.get('email')  
                category = request.POST.get('category')     
                password = encPassStr              

                #print(app_name,url,username,email,category,password)      

                try:
                    db = Passwords(user=user, app_name=app_name,url=url, username=username, email=email,password=password,category=category)
                    db.save()

                except:
                    print("Unable to save data") 

                return redirect('/')  
        return render(request, "create.html")

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
            
            user = request.user
            app_name = request.POST.get('app_name')
            url = request.POST.get('url')
            username = request.POST.get('username') 
            email = request.POST.get('email')  
            category = request.POST.get('category')     
            password = encPassStr              

            #print(app_name,url,username,email,category,password)      

            try:
                db = Passwords.objects.get(id=uid, user=user)

                db.user = user
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
        
    user = request.user
    viewPass = Passwords.objects.all().filter(id=uid, user= user)
    vals = list(viewPass.values())
    vals = vals[0]

    passKey = vals['password']
    data = vals

    hashedPass = passKey.encode('latin-1')
    actual = UnhashPassword(hashedPass=hashedPass)

    return render(request,'view-password.html', {'form':data,'password':actual, 'name':'View Password | PyPassManager'})

def logout_user(request):
    logout(request)
    return redirect("/login/")

def create_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            form = auth_login(request, user)
            return redirect("/")
        else:
            messages.add_message(request, messages.ERROR, 'Wrong Password')
            print("Invalid Form")
            return render (request=request, template_name="register.html", context={"register_form":form})

    else:
        form = NewUserForm()
        return render (request=request, template_name="register.html", context={"register_form":form})
