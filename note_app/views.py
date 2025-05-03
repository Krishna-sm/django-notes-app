from django.shortcuts import render

# Create your views here.

def indexView(req):
    return render(req,"index.html")

def notesView(req):
    return render(req,"notes/notes.html",context={'cards': range(10)})


def loginView(req):
    return render(req,"auth/login.html")

def registerView(req):
    return render(req,"auth/register.html")