from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# def filmes(request):
#     return render(request,"filmes.html")

def filmes_lista(request):
    genero = request.GET.get("genero")
    filmes = [...]  # seu código de filmes aqui
    if genero:
        filmes = [f for f in filmes if f["genero"] == genero]
    return render(request, "filmes_lista.html", {"filmes": filmes, "genero": genero})


def filmes_roleta(request):
    return render(request, "filmes_roleta.html")
