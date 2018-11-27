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

urlpatterns = [
    path('home', views.index, name="home"),
    #contenido estatico
    path('pago', views.pago, name="pago" ),
    #tags
    path('tags', views.tags, name="tags"),
    path('crear_tag', views.crear_tag, name='crear_tag'),
    path('editar_tag', views.editar_tag, name='editar_tag'),
    path('eliminar_tag', views.eliminar_tag, name='eliminar_tag'),
    #noticias
    path('noticias', views.noticias, name="noticias"),
    path('crear_noticia', views.crear_noticia, name='crear_noticia'),
    #eventos
    path('eventos', views.eventos, name="eventos"),
    path('crear_evento', views.crear_evento, name='crear_evento'),
    #tareas
    path('tareas', views.tareas, name="tareas"),
    path('crear_tarea', views.crear_tarea, name='crear_tarea'),
    #registro
    path('login', auth_views.LoginView.as_view(), name="login"),
    path('logout', auth_views.LogoutView.as_view(), name="logout"),
    #evento

]
