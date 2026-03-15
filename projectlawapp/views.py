from django.shortcuts import render, redirect
from . models import ProjectLawModel
from . forms import ProjectLawForms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def home(request):
    myData = ProjectLawModel.objects.all()
    return render(request, 'home.html',
                  {
                      'myData':myData
                  })

def forms(request):
    myForm = ProjectLawForms()
    if request.method == 'POST':
        myForm = ProjectLawForms(request.POST, request.FILES)
        if myForm.is_valid():
            myForm.save()
            return redirect('home')
    return render(request, 'forms.html',
                          {
                              'myForm':myForm
                        })

def RegistrationForm(request):
    RegisterUser = UserCreationForm()
    if request.method == 'POST':
        RegisterUser = UserCreationForm(request.POST)
        if RegisterUser.is_valid():
            RegisterUser.save()
            return redirect('LoginForm')
    return render(request, 'RegistrationForm.html',
                  {
                      'RegisterUser':RegisterUser
                  })

def LoginForm(request):
    if request.method == 'POST':
        TheUsername = request.POST['username']
        ThePassword = request.POST['password']
        TheUser = authenticate(request, username=TheUsername, password=ThePassword)
        if TheUser:
            login(request, TheUser)
            return redirect('home')
    return render(request, 'login.html')

