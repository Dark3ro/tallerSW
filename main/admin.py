from django.contrib import admin
from .models import Tarea, Tag, Usuario, Noticia
# Register your models here.

admin.site.register(Tarea)
admin.site.register(Tag)
admin.site.register(Usuario)
admin.site.register(Noticia)
