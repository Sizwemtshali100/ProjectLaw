from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.LoginForm, name='LoginForm'),    
    path('home/', views.home, name='home'),
    path('forms/', views.forms, name='forms'),
    path('RegistrationForm/', views.RegistrationForm, name='RegistrationForm'),
]
