from app.models import Category, Post
from app.serializers import CatAndPostsSerializer, PostSerializer
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CatAndPosts(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CatAndPostsSerializer

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = CatAndPostsSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = Category.objects.all()
    #     cat = get_object_or_404(queryset, pk=pk)
    #     serializer = CatAndPostsSerializer(cat)
    #     return Response(serializer.data)



