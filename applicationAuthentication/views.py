from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login, logout

def signup_page(request):   
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'applicationAuthentication/signup.html', {'form': form})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrec')
    context = {}
    return render(request, 'applicationAuthentication/login.html', context)

def logout_page(request):
    logout(request)
    return redirect('home')

#@login_required(login_url='login')
def home(request):   
    return render(request, 'applicationAuthentication/home.html')

