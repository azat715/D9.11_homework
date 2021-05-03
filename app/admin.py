from app.models import Category, Post
from django.contrib import admin


@admin.register(Post)
class Post(admin.ModelAdmin):
    pass


@admin.register(Category)
class Category(admin.ModelAdmin):
    pass
