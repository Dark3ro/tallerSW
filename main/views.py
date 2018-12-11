from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Tag, Noticia, Evento, Proyecto
#
from django.contrib import messages
from .forms import NoticiaForm


#@login_required()
def crea_noti(request):
    if request.method == 'POST':
        if form.is_valid():
            noticia = Noticia()
            noticia.titulo = request.POST.get('titulo')
            noticia.texto = request.POST.get('texto')
            noticia.save()
            tags = request.POST.get('tag_name', '')
            noticia.tag.add(tags)
            messages.success(request, 'La noticia fue creada correctamente')
        else:
            messages.warning(request, 'Falta ingresar un dato')
    return redirect('noticias')


# Create your views here.
#@login_required()
def index(request):
    return render(request, 'home.html')

#@login_required()
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            form = UserCreationForm()
            args = {'form':form}
            return render(request, 'registration/reg_form.html', args)


#----------------------------------------------------------------------
#@login_required()
def tags(request):
    tags = Tag.objects.all()
    return render(request, 'tags.html', {'tags':tags})

#@login_required()
def agregar_tags(request):
    tags = Tag.objects.all()
    return render(request, 'agregar_tags.html', {'tags':tags})

#@login_required()
def crear_tag(request):
    if request.method == 'POST':
        tag = Tag()
        tag.name_tag = request.POST.get('name_tag')
        tag.save()
    return redirect('tags')

#@login_required()
def modificar_tags(request):
    tags = Tag.objects.all()
    return render(request, 'modificar_tags.html', {'tags':tags})

#@login_required()
def editar_tag(request):
    if request.method == 'POST':
        id = request.POST.get('id_tag')
        print('id: ',id)
        tag = Tag.objects.get(pk=id)
        tag.name_tag = request.POST.get('name_tag')
        tag.save()
    return redirect('tags')

#@login_required()
def borrar_tags(request):
    tags = Tag.objects.all()
    return render(request, 'borrar_tags.html', {'tags':tags})

#@login_required()
def eliminar_tag(request):
    if request.method == 'POST':
        id = request.POST.get('id_tag')
        tag = Tag.objects.get(pk=id)
        tag.delete()
    return redirect('tags')


#----------------------------------------------------------------------
#@login_required()
def noticias(request):
    tags = Tag.objects.all()
    noticias = Noticia.objects.all()
    return render(request, 'noticias.html', {'tags':tags, 'noticias':noticias})

#@login_required()
def agregar_noticia(request):
    tags = Tag.objects.all()
    noticias = Noticia.objects.all()
    return render(request, 'agregar_noticia.html',{'tags':tags,'noticias':noticias})

#@login_required()
def crear_noticia(request):
    if request.method == 'POST':
        noticia = Noticia()
        noticia.titulo = request.POST.get('titulo')
        noticia.texto = request.POST.get('texto')
        noticia.save()
        tags = request.POST.get('tag_name', '')
        noticia.tag.add(tags)
    return redirect('noticias')

#@login_required()
def modificar_noticia(request):
    tags = Tag.objects.all()
    noticias = Noticia.objects.all()
    return render(request, 'modificar_noticia.html',{'tags':tags,'noticias':noticias})

#@login_required()
def editar_noticia(request):
    if request.method == 'POST':
        id = request.POST.get('id_noticia')
        noticia = Noticia.objects.get(pk=id)
        noticia.titulo = request.POST.get('titulo_edit')
        noticia.texto = request.POST.get('texto_edit')
        noticia.save()
    return redirect('noticias')

#@login_required()
def mostrar_noticia(request):
    if request.method == 'POST':
        id = request.POST.get('id_noticia')
        noticia = Noticia.objects.get(pk=id)
    return render(request, 'modificar_noticia.html', {'noticia':noticia})

#@login_required()
def borrar_noticia(request):
    noticias = Noticia.objects.all()
    return render(request, 'borrar_noticia.html',{'noticias':noticias})

#@login_required()
def eliminar_noticia(request):
    if request.method == 'POST':
        id = request.POST.get('id_noticia')
        noticia = Noticia.objects.get(pk=id)
        noticia.delete()
    return redirect('noticias')
#----------------------------------------------------------------------
#@login_required()
def eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos.html', {'eventos':eventos})

#@login_required()
def agregar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'agregar_eventos.html', {'eventos':eventos})

#@login_required()
def crear_evento(request):
    if request.method == 'POST':
        evento = Evento()
        evento.nombre = request.POST.get('nombre')
        evento.auspicio = request.POST.get('auspicio')
        evento.fecha = request.POST.get('fecha')
        evento.save()
    return redirect('eventos.html')

#@login_required()
def modificar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'modificar_eventos.html', {'eventos':eventos})

#@login_required()
def editar_evento(request):
    if request.method == 'POST':
        id = request.POST.get('id_evento')
        evento = Evento.objects.get(pk=id)
        evento.nombre = request.POST.get('nombre_edit')
        evento.auspicio = request.POST.get('auspicio_edit')
        evento.fecha = request.POST.get('fecha_edit')
        evento.save()
    return redirect('eventos')

#@login_required()
def mostrar_evento(request):
    if request.method == 'POST':
        id = request.POST.get('id_evento')
        evento = Evento.objects.get(pk=id)
    return render(request, 'modificar_eventos.html', {'evento':evento})

#@login_required()
def borrar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'borrar_eventos.html', {'eventos':eventos})

#@login_required()
def eliminar_evento(request):
    if request.method == 'POST':
        id = request.POST.get ('id_evento')
        evento = Evento.objects.get(pk=id)
        evento.delete()
    return redirect('eventos')
#----------------------------------------------------------------------
#@login_required()
def proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyectos.html', {'proyectos':proyectos})

#@login_required()
def crear_proyecto(request):
    if request.method == 'POST':
        proyecto = Proyecto()
        proyecto.nombre_pro = request.POST.get('nombre')
        proyecto.tipo = request.POST.get('tipo')
        proyecto.save()
    return redirect('proyectos')

#@login_required()
def editar_proyecto(request):
    if request.method == 'POST':
        id = request.POST.get('id_proyecto')
        proyecto = Proyecto.objects.get(pk=id)
        proyecto.nombre_pro = request.POST.get('nombre_pro')
        proyecto.tipo = request.POST.get('tipo')
        proyecto.save()
    return redirect('proyectos')

#@login_required()
def eliminar_proyecto(request):
    if request.method == 'POST':
        id = request.POST.get('id_proyecto')
        proyecto = Proyecto.objects.get(pk=id)
        proyecto.delete()
    return redirect('proyectos')
#----------------------------------------------------------------------
#@login_required()
def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios.html', {'usuarios':usuarios})

#@login_required()
def crear_usuario(request):
    if request.method == 'POST':
        usuario = Usuario()
        usuarios.nombre_pro = request.POST.get('nombre')
        usuarios.tipo = request.POST.get('tipo')
        usuarios.save()
    return redirect('usuarios')

#-----------------------------------------------------------------------
#@login_required()
def pago(request):
    return render(request, 'pago.html')
#@login_required()
def publico(request):
    return render(request, 'publico.html')
#@login_required
def quienes_somos(request):
    return render(request,'quienes_somos.html')
#@login_required
def posicionamiento(request):
    return render(request,'posicionamiento.html')
#@login_required
def servicios(request):
    return render(request, 'servicios.html')
#@login_required
def retribucion(request):
    return render(request, 'retribucion.html')
#@login_required
def prototipado(request):
    return render(request, 'prototipado.html')
#@login_required
def area_extension(request):
    return render(request, 'area_extension.html')
#@login_required
def membresia(request):
    return render(request, 'membresia.html')
#@login_required
def investigacion(request):
    return render(request, 'investigacion.html')
