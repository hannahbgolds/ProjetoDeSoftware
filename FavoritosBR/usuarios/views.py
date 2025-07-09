from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import FilmeDeUmUsuario
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.utils import timezone

@login_required
def meus_filmes(request):
    aba = request.GET.get("aba", "favoritos")
    user = request.user

    favoritos = FilmeDeUmUsuario.objects.filter(user=user, status='nao-assistido').order_by('-created_at')
    assistidos = FilmeDeUmUsuario.objects.filter(user=user, status='assistido').order_by('-assistiu_at')

    return render(request, 'meus_filmes.html', {
        'favoritos': favoritos,
        'assistidos': assistidos,
        'aba': aba
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


@csrf_exempt
@login_required
def marcar_como_assistido(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            filme_id = data.get("filme_id_api")

            if not filme_id:
                return JsonResponse({"erro": "ID do filme ausente."}, status=400)

            filme = FilmeDeUmUsuario.objects.get(user=request.user, filme_id_api=filme_id)
            filme.status = "assistido"
            filme.assistiu_at = timezone.now()

            nota = data.get("nota")
            if nota is not None:
                try:
                    filme.nota = int(nota)
                except ValueError:
                    pass 

            filme.save()

            return JsonResponse({"sucesso": True})
        except FilmeDeUmUsuario.DoesNotExist:
            return JsonResponse({"erro": "Filme não encontrado para o usuário."}, status=404)
        except Exception as e:
            return JsonResponse({"erro": str(e)}, status=500)

    return JsonResponse({"erro": "Método não permitido."}, status=405)
