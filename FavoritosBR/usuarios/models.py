from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class FilmeFavoritado(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favoritos')
    filme_id_api = models.IntegerField()
    titulo = models.CharField(max_length=255)

    class Meta:
        unique_together = ('user', 'filme_id_api')

    def __str__(self):
        return f"{self.titulo} (favoritado por {self.user.username})"


class FilmeAssistido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assistidos')
    filme_id_api = models.IntegerField()
    titulo = models.CharField(max_length=255)

    class Meta:
        unique_together = ('user', 'filme_id_api')

    def __str__(self):
        return f"{self.titulo} (assistido por {self.user.username})"
    
class FilmeDeUmUsuario(models.Model):
    STATUS_CHOICES = [
        ('nao-assistido', 'Não Assistido'),
        ('assistido', 'Assistido'),
    ]
    username = models.CharField(max_length=50)
    titulo = models.CharField(max_length=100)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='nao-assistido')
    nota = models.IntegerField(choices=[(i, i) for i in range(0, 6)])
    created_at = models.DateTimeField(auto_now_add=True)
    assistiu_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} ({self.username})"