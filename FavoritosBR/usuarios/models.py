from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class FilmeDeUmUsuario(models.Model):
    STATUS_CHOICES = [
        ('nao-assistido', 'Não Assistido'),
        ('assistido', 'Assistido'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="filmes")
    filme_id_api = models.IntegerField()  # ID do TMDb
    titulo = models.CharField(max_length=255)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='nao-assistido')
    nota = models.IntegerField(choices=[(i, i) for i in range(0, 6)], blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    assistiu_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'filme_id_api')

    def __str__(self):
        return f"{self.titulo} - {self.user.username} ({self.status})"
