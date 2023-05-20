from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import InputValue
from datetime import date
from .forms import InputForm
import json


def home(request):
    return render(request, 'fintess_app/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('fintess_app:home')
        else:
            return redirect('login')
    return render(request, 'fintess_app/login.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'fintess_app/sign_up.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'fintess_app/home.html')

def profile_view(request):
    form = InputForm(request.POST or None)

    if form.is_valid():
        if request.user.is_authenticated:
            input_data = form.save(commit=False)
            input_data.user = request.user
            input_data.save()
            return redirect('fintess_app:profile')
        else:
            return redirect('fintess_app:login')  # Redirect to login page if user is not authenticated

    input_data = InputValue.objects.filter(user=request.user).order_by('date')

    dates = [data.date.strftime('%Y-%m-%d') for data in input_data]
    dates_json = json.dumps(dates)
    values = [data.value for data in input_data]

    context = {
        'form': form,
        'dates': dates_json,
        'values': values,
    }

    return render(request, 'fintess_app/profile.html', context)