from django.contrib import admin

from app.models import Post, Category


@admin.register(Post)
class Post(admin.ModelAdmin):
    pass

@admin.register(Category)
class Category(admin.ModelAdmin):
    pass