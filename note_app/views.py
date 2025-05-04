from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Note


# Create your views here.

def indexView(req):
    if not req.user.is_authenticated:
        return redirect("/login/")
    if req.method=='POST':
        title = req.POST.get("title","").strip()
        description = req.POST.get("description","").strip()
        
        if not title or not description:
            messages.error(req,"Fill All Details")
            return redirect("/")
        
        note = Note.objects.create(title=title,description=description,user=req.user)
        
        messages.success(req,"Note Created :)")
        return redirect("/")

        
    return render(req,"index.html")

def notesView(req):
    if not req.user.is_authenticated:
        return redirect("/login/")
    notes = Note.objects.filter(user=req.user)
    return render(req,"notes/notes.html",context={'cards': notes})


def loginView(req):
    if req.method == 'POST':
        email = req.POST.get("email","").strip().lower()
        password = req.POST.get("password","")
        
        if not email or not password:
            messages.error(req,"Fill All Fields")
            return redirect("/login/")
        if not User.objects.filter(email=email).exists():
            messages.error(req,"Account Not Found")
            return redirect("/login/")
        # check invalid password 
    
        user = authenticate(req,username =email ,password =password)
        if user is not None:
            login(req,user)
            # messages.success(req,"Login Success")
            return redirect("/")
        else:
            messages.error(req,"Invalid Credentials")
            return redirect("/login/")

        

    return render(req,"auth/login.html")

def registerView(req):
    if req.method =='POST':
        name = req.POST['name'] or ''
        email = req.POST['email'] or ''
        password = req.POST['password'] or ''
        if not name or not email or not password:
            messages.error(req,"Fill All Required Fileds")
            return redirect("/register/")
        email = email.strip().lower()
        
        # check user is exist or not if have then show error 
        
        if User.objects.filter(email = email).exists():
            messages.error(req,"User Already Exists")
            return redirect("/register/")
        # create new user   
        user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=name
        ) 
        user.save()
        messages.success(req,"User Register Successfully ")
        
        
    
    return render(req,"auth/register.html")


def logoutView(req):
    logout(req)
    messages.success(req,"Logout Success")
    return redirect("/login/")