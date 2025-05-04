from django.urls import path
from .views import loginView,registerView,indexView,notesView,logoutView
urlpatterns=[
    path("",indexView,name="index"),
    path("login/",loginView,name="login"),
    path("register/",registerView,name="register"),
    path("notes/",notesView,name="notes"),
    path("logout/",logoutView,name="logout")
]