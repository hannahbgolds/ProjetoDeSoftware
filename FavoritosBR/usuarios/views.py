from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import FilmeFavoritado, FilmeAssistido


def meus_filmes(request):
    user = request.user
    favoritos = FilmeFavoritado.objects.filter(user=user)
    assistidos = FilmeAssistido.objects.filter(user=user)
    return render(request, 'meus_filmes.html', {
        'favoritos': favoritos,
        'assistidos': assistidos
    })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Substitua pelo nome da sua URL inicial
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})