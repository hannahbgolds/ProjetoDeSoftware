from django.db import models

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

