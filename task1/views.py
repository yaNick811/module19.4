from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Buyer, Game

def index(request):
    return render(request, 'index.html')

def games(request):
    games_list = Game.objects.all()
    return render(request, 'games.html', {'games_list': games_list})

def cart(request):
    return render(request, 'cart.html')

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            age = form.cleaned_data['age']

            # Проверяем, существует ли пользователь с таким именем
            if not Buyer.objects.filter(name=username).exists():
                Buyer.objects.create(name=username, balance=0.0, age=age)
                return redirect('index')
            else:
                return render(request, 'registration.html', {'form': form, 'error': 'Пользователь с таким именем уже существует'})
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})