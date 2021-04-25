from app.models import Category, Post
from app.serializers import CatAndPostsSerializer, PostSerializer
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CatAndPosts(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CatAndPostsSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CatAndPostsSerializer(queryset, many=True)
        return Response(serializer.data)
