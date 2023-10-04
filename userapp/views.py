from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from userapp.forms import CustomUser

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUser(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('index')
        else:
            return redirect('signup')
    else:
        form = CustomUser()
        return render(request, 'signup.html', {'form': form})
    
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    
def logout(request):
    auth.logout(request)
    return redirect('index')