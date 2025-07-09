from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
import requests
from django.shortcuts import render
from django.http import JsonResponse
from usuarios.models import FilmeDeUmUsuario
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

TMDB_API_TOKEN = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMWQ1MDExZGNkYWI3ZjU0OGRhNDM4ZmRhMjRjN2ViZCIsIm5iZiI6MTc1MDk5MTcxMC44NTY5OTk5LCJzdWIiOiI2ODVlMDM1ZWMwNjZhNDk0YzEzNGYyZDEiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.bc5-4RE8_UXxp5d617Cw2LJfowA3x70_z_rVrU3hsa8"

GENRE_MAP = {
    "Ação": 28,
    "Comédia": 35,
    "Drama": 18,
    "Romance": 10749
}

@login_required
def filmes_lista(request):
    genero_nome = request.GET.get("genero")
    genero_id = GENRE_MAP.get(genero_nome)

    url = "https://api.themoviedb.org/3/discover/movie"
    headers = {
        "Authorization": TMDB_API_TOKEN,
        "accept": "application/json"
    }
    params = {
        "with_origin_country": "BR",
        "sort_by": "popularity.desc",
        "language": "pt-BR"
    }
    if genero_id:
        params["with_genres"] = genero_id

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    filmes_favoritados_ids = set(
        FilmeDeUmUsuario.objects.filter(user=request.user)
        .values_list('filme_id_api', flat=True)
    )

    filmes = []
    for filme in data.get("results", []):
        id_api = filme.get("id")
        filmes.append({
            "titulo": filme.get("title"),
            "filme_id_api": id_api,
            "ano": filme.get("release_date", "")[:4],
            "genero": genero_nome or "Vários",
            "poster": f"https://image.tmdb.org/t/p/w200{filme.get('poster_path')}" if filme.get("poster_path") else None,
            "favoritado": id_api in filmes_favoritados_ids
        })

    return render(request, "filmes_lista.html", {
        "filmes": filmes,
        "genero": genero_nome
    })

def filmes_roleta(request):
    return render(request, "filmes_roleta.html")

@csrf_exempt
@login_required
def marcar_nao_assistido(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            titulo = data.get("titulo")
            filme_id = data.get("filme_id_api")
            poster_url = data.get("poster_url")

            if not titulo or not filme_id:
                return JsonResponse({"erro": "Campos obrigatórios faltando."}, status=400)

            filme_obj = FilmeDeUmUsuario.objects.filter(user=request.user, filme_id_api=filme_id).first()

            if filme_obj:
                filme_obj.delete()
                return JsonResponse({"sucesso": True, "removido": True})
            else:
                FilmeDeUmUsuario.objects.create(
                    user=request.user,
                    titulo=titulo,
                    filme_id_api=filme_id,
                    poster=poster_url,
                    status='nao-assistido'
                )
                return JsonResponse({"sucesso": True, "removido": False})

        except json.JSONDecodeError:
            return JsonResponse({"erro": "JSON inválido."}, status=400)
    return JsonResponse({"erro": "Método não permitido."}, status=405)

def filmes_por_genero_api(request):
    genero = request.GET.get("genero")

    filmes = FilmeDeUmUsuario.objects.all()

    if genero:
        filmes = filmes.filter(Q(genero__iexact=genero) | Q(genero__icontains=genero))

    filmes_unicos = {}
    for f in filmes:
        if f.titulo not in filmes_unicos:
            filmes_unicos[f.titulo] = {
                "titulo": f.titulo,
                "poster": f.poster_url,
                "sinopse": f.sinopse or "",
                "diretor": f.diretor or "",
                "ano": f.data_lancamento.year if f.data_lancamento else "",
            }

    return JsonResponse(list(filmes_unicos.values()), safe=False)