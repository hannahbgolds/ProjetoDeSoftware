from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import FilmeDeUmUsuario

@login_required
def meus_filmes(request):
    user = request.user

    favoritos = FilmeDeUmUsuario.objects.filter(user=user, status='nao-assistido').order_by('-created_at')
    assistidos = FilmeDeUmUsuario.objects.filter(user=user, status='assistido').order_by('-assistiu_at')

    return render(request, 'meus_filmes.html', {
        'favoritos': favoritos,
        'assistidos': assistidos,
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