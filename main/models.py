from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField(max_length = 255)
    descripcion = models.CharField(max_length = 255)
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)

class Tag(models.Model):
    id_tag = models.AutoField(primary_key=True)
    name_tag = models.CharField(max_length = 255)

    def __str__(self):
        return self.id_tag

    class Meta:
        ordering = ('id_tag',)

class Usuario(models.Model):
    user= models.OneToOneField(User, on_delete = models.CASCADE)
    estado = models.CharField(max_length = 255)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.user

    class Meta:
        ordering = ('user',)

class Noticia(models.Model):
    id_noticia = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length = 255)
    texto = models.CharField(max_length = 1500)
    fecha= models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.id_noticia

    class Meta:
        ordering = ('id_noticia',)

class Tipo(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 255)

    def __str__(self):
        return self.id_tipo

    class Meta:
        ordering = ('id_tipo',)

class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 255)
    auspicio = models.CharField(max_length = 255)
    fecha = models.CharField(max_length = 10)

    def __str__(self):
        return self.id_evento

    class Meta:
        ordering = ('id_evento',)
