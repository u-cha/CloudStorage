from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render

from .forms import LoginForm, RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a home page after registration
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to a home page after login
        else:
            return render(request, 'registration/login.html', {'form': form})  # Render with errors
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, "You logged out from CloudStorage. Have a nice day!")
        return redirect('home')
    if request.method == 'GET':
        return render(request, 'registration/logout.html', {})
