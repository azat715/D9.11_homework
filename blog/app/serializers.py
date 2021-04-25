from app.models import Category, Post
from django.contrib.auth.models import User
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False)

    class Meta:
        model = Post
        fields = "__all__"


class CatAndPostsSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, required=False)

    class Meta:
        model = Category
        fields = "__all__"

    def create(self, validated_data):
        posts_data = validated_data.pop("posts")
        category = Category.objects.create(**validated_data)
        for post_data in posts_data:
            author_data = post_data.pop("author", None)
            if author_data:
                if not User.objects.filter(username=author_data["username"]).exists():
                    author = User.objects.create(**author_data)
                else:
                    author = User.objects.get(username=author_data["username"])
                Post.objects.create(category=category, author=author, **post_data)
            else:
                Post.objects.create(category=category, **post_data)
        return category
