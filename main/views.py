from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Tarea, Tag, Noticia

# Create your views here.
@login_required()
def index(request):
    return redirect('tareas')

@login_required()
def pago(request):
    return render(request, 'pago.html')
#----------------------------------------------------------------------
@login_required()
def tags(request):
    tags = Tag.objects.all()
    return render(request, 'tags.html', {'tags':tags})

@login_required()
def crear_tag(request):
    if request.method == 'POST':
        tag = Tag()
        tag.name_tag = request.POST.get('name_tag')
        tag.save()
    return redirect('tags')

@login_required()
def editar_tag(request):
    if request.method == 'POST':
        id = request.POST.get('id_tag')
        tag = Tag.objects.get(pk=id)
        tag.name_tag = request.POST.get('name_tag')
        tag.save()
    return redirect('tags')

@login_required()
def eliminar_tag(request):
    if request.method == 'POST':
        id = request.POST.get('id_tag')
        tag = Tag.objects.get(pk=id)
        tag.delete()
    return redirect('tags')
#----------------------------------------------------------------------
@login_required()
def noticias(request):
    tags = Tag.objects.all()
    noticia = Noticia.objects.all()
    return render(request, 'noticias.html', {'tags':tags, 'noticias':noticias})

@login_required()
def crear_noticia(request):
    if request.method == 'POST':
        noticia = Noticia()
        noticia.titulo = request.POST.get('titulo')
        noticia.texto = request.POST.get('texto')
        noticia.save()
        tags = request.POST.get('tag_name', '')
        noticia.tag.add(tags)
    return redirect('noticias')
#----------------------------------------------------------------------


#----------------------------------------------------------------------
@login_required()
def tareas(request):
    tareas = Tarea.objects.filter(usuario=request.user)
    return render(request, 'tareas.html', {'tareas':tareas})

@login_required()
def crear_tarea(request):
    if request.method == 'POST':
        tarea = Tarea()
        tarea.titulo = request.POST.get('titulo_tarea')
        tarea.descripcion = request.POST.get('desc_tarea')
        tarea.usuario = request.user
        tarea.save()
    return redirect('tareas')
