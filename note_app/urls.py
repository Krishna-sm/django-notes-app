from django.urls import path
from .views import loginView,registerView,indexView,notesView
urlpatterns=[
    path("",indexView,name="index"),
    path("login/",loginView,name="login"),
    path("register/",registerView,name="register"),
    path("notes/",notesView,name="notes")
]