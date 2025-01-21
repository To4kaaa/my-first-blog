from django.contrib import admin
from .models import Post
# Импортируем модель Post которая находится в models
admin.site.register(Post)
