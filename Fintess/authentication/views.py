from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from datetime import date
from .models import WeightEntry
import json
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authentication:login')
    else:
        form = UserCreationForm()
    return render(request, 'authentication/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('authentication:home')
        else:
            return redirect('authentication:login.html')
    return render(request, 'authentication/login.html')

@login_required
def weight_track(request):
    last_weight = request.session.get('last_weight')

    if request.method == 'POST':
        weight = float(request.POST.get('weight'))
        entry = WeightEntry(weight=weight)
        entry.save()
        request.session['last_weight'] = weight
        return redirect('authentication:weight_track')

    weight_entries = WeightEntry.objects.all().order_by('-date')
    weight_data = [
        {
            'date': entry.date.strftime('%Y-%m-%d'),
            'weight': float(entry.weight)
        }
        for entry in weight_entries
    ]
    weight_data_json = json.dumps(weight_data)

    return render(request, 'authentication/weight_track.html', {'weight_entries': weight_entries, 'weight_data_json': weight_data_json, 'last_weight': last_weight})

def update_weight(request):
    if request.method == 'POST':
        # Retrieve the weight value from the form
        weight = float(request.POST.get('weight'))

        # Get the current date
        current_date = date.today().strftime('%Y-%m-%d')

        # Create a dictionary containing the date and weight
        data_point = {
            'date': current_date,
            'weight': weight
        }

        # Save the data point or do any other processing

        # Return a JSON response with the data point
        return JsonResponse(data_point)
    else:
        return JsonResponse({'error': 'Invalid request'})

def home(request):
    return render(request, 'authentication/home.html')

def logout_view(request):
    logout(request)
    return render(request, 'authentication/home.html')