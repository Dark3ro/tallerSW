"""tallerSW URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name="home"),
    #contenido estatico
    path('pago', views.pago, name="pago" ),
    path('publico', views.publico, name="publico"),
    path('quienes_somos',views.quienes_somos, name='quienes_somos'),
    path('posicionamiento',views.posicionamiento, name='posicionamiento'),
    path('servicios',views.servicios, name='servicios'),
    path('retribucion', views.retribucion, name='retribucion'),
    path('prototipado', views.prototipado, name='prototipado'),
    path('area_extension', views.area_extension, name='area_extension'),
    path('membresia',views.membresia, name='membresia'),
    path('investigacion',views.investigacion, name='investigacion'),
    #tags
    path('tags', views.tags, name="tags"),
    path('agregar_tags',views.agregar_tags, name='agregar_tags'),
    path('crear_tag', views.crear_tag, name='crear_tag'),
    path('editar_tags', views.modificar_tags, name='modificar_tags'),
    path('editar_tag', views.editar_tag, name='editar_tag'),
    path('eliminar_tags', views.borrar_tags, name='borrar_tags'),
    path('eliminar_tag', views.eliminar_tag, name='eliminar_tag'),

    #noticias
    path('noticias', views.noticias, name="noticias"),
    path('agregar_noticia',views.agregar_noticia, name='agregar_noticia'),
    path('crear_noticia', views.crear_noticia, name='crear_noticia'),
    path('modificar_noticia', views.modificar_noticia, name='modificar_noticia'),
    path('editar_noticia', views.editar_noticia, name='editar_noticia'),
    path('mostrar_noticia', views.mostrar_noticia, name='mostrar_noticia'),
    path('eliminar_noticia', views.borrar_noticia, name='borrar_noticia'),
    path('eliminar_noticia', views.eliminar_noticia, name='eliminar_noticia'),

    #proyectos
    path('proyectos', views.proyectos, name="proyectos"),
    path('crear_proyecto', views.crear_proyecto, name='crear_proyecto'),
    path('editar_proyecto', views.editar_proyecto, name='editar_proyecto'),
    path('eliminar_proyecto', views.eliminar_proyecto, name='eliminar_proyecto'),

    #eventos
    path('eventos', views.eventos, name="eventos"),
    path('agregar_eventos', views.agregar_eventos, name='agregar_eventos'),
    path('crear_evento', views.crear_evento, name='crear_evento'),
    path('editar_eventos', views.modificar_eventos, name='modificar_eventos'),
    path('editar_evento', views.editar_evento, name='editar_evento'),
    path('mostrar_evento', views.mostrar_evento, name='mostrar_evento'),
    path('borrar_eventos', views.borrar_eventos, name='borrar_eventos'),
    path('eliminar_evento', views.eliminar_evento, name='eliminar_evento'),

    #registro
    path('login', auth_views.LoginView.as_view(), name="login"),
    path('logout', auth_views.LogoutView.as_view(), name="logout"),
    path('registro', views.registro, name="registro"),
    #
    path('crea_noti', views.crea_noti, name='crea_noti'),

]
