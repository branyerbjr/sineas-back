from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
