from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
import requests
from django.shortcuts import render

TMDB_API_TOKEN = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMWQ1MDExZGNkYWI3ZjU0OGRhNDM4ZmRhMjRjN2ViZCIsIm5iZiI6MTc1MDk5MTcxMC44NTY5OTk5LCJzdWIiOiI2ODVlMDM1ZWMwNjZhNDk0YzEzNGYyZDEiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.bc5-4RE8_UXxp5d617Cw2LJfowA3x70_z_rVrU3hsa8"

GENRE_MAP = {
    "Ação": 28,
    "Comédia": 35,
    "Drama": 18,
    "Romance": 10749
}

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

    filmes = []
    for filme in data.get("results", []):
        filmes.append({
            "titulo": filme.get("title"),
            "ano": filme.get("release_date", "")[:4],
            "genero": genero_nome or "Vários",
            "poster": f"https://image.tmdb.org/t/p/w200{filme.get('poster_path')}" if filme.get("poster_path") else None
        })

    return render(request, "filmes_lista.html", {
        "filmes": filmes,
        "genero": genero_nome
    })

def filmes_roleta(request):
    return render(request, "filmes_roleta.html")
