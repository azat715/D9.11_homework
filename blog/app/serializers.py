from rest_framework import serializers
from django.contrib.auth.models import User

from app.models import Post
 

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class PostSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(required=False)  

    class Meta:
        model = Post
        fields = '__all__'



    