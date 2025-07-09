from django.urls import path
from . import views
from .views import filmes_lista, filmes_roleta, marcar_nao_assistido


urlpatterns = [
    path("", views.filmes_lista, name="filmes"),
    path("roleta/", views.filmes_roleta, name="filmes_roleta"),
    path("marcar_nao_assistido/", views.marcar_nao_assistido, name="marcar_nao_assistido"),
    path("api/filmes/", views.filmes_por_genero_api, name="filmes_por_genero_api"),
]
