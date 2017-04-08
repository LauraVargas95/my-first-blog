from django.contrib import admin

from .models import Post #del archivo de models se importa Post

admin.site.register(Post)# Se incluye el modelo Post


