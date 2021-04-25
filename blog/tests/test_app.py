# from django.test import TestCase

# # Create your tests here.
import pytest

from unittest import mock

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
from django.urls import reverse 
from datetime import datetime

from app.models import Category, Post
from app.serializers import PostSerializer
from app.views import PostList
from app.models import timezone 

from .conftest import content, api_client

@pytest.mark.django_db
@pytest.fixture
def user_client():
    """
    создание автора 
    """
    return User.objects.create_user(
        username='test_user',
        password='pass',
        first_name='Normal',
        last_name='User'
    )


@pytest.mark.django_db
def test_post_create(user_client):
    """
    создание post
    """

    category = Category.objects.create(name = 'Test_category')
    dt = datetime(2020, 1, 1, tzinfo=timezone.utc)
    post = Post.objects.create(
        title = 'Test title', 
        status = 'D', 
        content = 'Test text',
        updated = dt,
        publication_date = dt,
        category = category, 
        author = user_client
    )
    assert post.id == 1
    assert post.title == 'Test title'
    assert post.status == 'D'
    assert post.content == 'Test text'
    assert post.updated == dt
    assert post.publication_date == dt
    assert post.author.username == 'test_user'
    assert post.category.name == 'Test_category'
    assert post.status == 'D'
    assert post.slug == slugify(post.title)
    post.status = 'P'
    post.save()
    assert post.status == 'P'
    post.status = 'E'
    post.save()
    with pytest.raises(ValidationError):
        post.full_clean()


"""
тестирование views app
"""
@pytest.mark.django_db
def test_all_post(content, api_client):
    response = api_client.get(reverse('app:posts', current_app='app'))
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    assert response.data == serializer.data
    assert response.status_code == 200


@pytest.mark.django_db
def test_first_post(content, api_client):
    response = api_client.get(reverse('app:post-detail', args=[1], current_app='app'))
    post = Post.objects.first()
    serializer = PostSerializer(post)
    assert response.data == serializer.data
    assert response.status_code == 200

