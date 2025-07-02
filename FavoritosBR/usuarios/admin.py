from django.contrib import admin
from usuarios.models import FilmeFavoritado, FilmeAssistido
from usuarios.models import FilmeDeUmUsuario

admin.site.register(FilmeFavoritado)
admin.site.register(FilmeAssistido)
admin.site.register(FilmeDeUmUsuario)
