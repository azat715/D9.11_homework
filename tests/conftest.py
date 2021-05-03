import pytest
from app.models import Category, Post
from django.contrib.auth.models import User
from rest_framework.test import APIClient

# from django.core.serializers import serialize




@pytest.fixture(scope="session")
def content(django_db_setup, django_db_blocker):
    """
    заполение базы данных
    """
    with django_db_blocker.unblock():
        user = User.objects.create_user(
            username="test_user", password="pass", first_name="Normal", last_name="User"
        )
        cat1 = Category.objects.create(name="Lorem ipsum dolor sit amet")
        cat2 = Category.objects.create(name="consectetur adipiscing elit")
        Post.objects.create(
            title="Lorem ipsum dolor sit amet,",
            status="D",
            content="""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.""",
            category=cat1,
            author=user,
        )
        Post.objects.create(
            title="cillum dolore eu fugiat nulla pariatur",
            status="P",
            content="""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.""",
            category=cat2,
            author=user,
        )
        Post.objects.create(
            title="Duis aute irure dolor",
            status="D",
            content="""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.""",
            category=cat1,
            author=user,
        )
        # fixture = serialize('json', list(User.objects.all()) + list(Category.objects.all()) + list(Post.objects.all()))
        # with open('fixture.json', 'w') as f:
        #     f.write(fixture)


@pytest.fixture(scope="session")
def api_client():
    return APIClient()


@pytest.fixture
def cat_posts_data():
    return {
        "name": "Excepteur sint occaecat",
        "posts": [
            {
                "title": "cillum dolore eu fugiat nulla pariatur2",
                "status": "D",
                "content": """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.""",
                "author": {"username": "test_user2", "password": "pass"},
            },
            {
                "title": "cillum dolore eu fugiat nulla pariatur3",
                "status": "D",
                "content": """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.""",
            },
        ],
    }
