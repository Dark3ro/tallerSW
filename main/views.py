from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Tarea, Tag, Noticia, Tipo, Evento

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
        print('id: ',id)
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
    noticias = Noticia.objects.all()
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

@login_required()
def editar_noticia(request):
    if request.method == 'POST':
        id = request.POST.get('id_noticia')
        noticia = Noticia.objects.get(pk=id)
        noticia.titulo = request.POST.get('titulo_edit')
        noticia.texto = request.POST.get('texto_edit')
        noticia.save()
    return redirect('noticias')

@login_required()
def mostrar_noticia(request):
    if request.method == 'POST':
        id = request.POST.get('id_noticia')
        noticia = Noticia.objects.get(pk=id)
    return render(request, 'noticias.html', {'noticia':noticia})

@login_required()
def eliminar_noticia(request):
    if request.method == 'POST':
        id = request.POST.get('id_noticia')
        noticia = Noticia.objects.get(pk=id)
        noticia.delete()
    return redirect('noticias')    
#----------------------------------------------------------------------
@login_required()
def eventos(request):
    tipos =Tipo.objects.all()
    evento = Evento.objects.all()
    return render(request, 'eventos.html', {'tipos':tipos, 'eventos':eventos})

@login_required()
def crear_evento(request):
    if request.method == 'POST':
        evento = Evento()
        evento.nombre = request.POST.get('nombre')
        evento.auspicio = request.POST.get('auspicio')
        evento.fecha = request.POST.get('fecha')
        evento.save()
    return redirect('eventos')


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
