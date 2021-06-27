from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()

# Create your models here.
