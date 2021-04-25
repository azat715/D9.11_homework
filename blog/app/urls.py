from app.views import CatAndPosts, PostDetail, PostList
from django.urls import path

app_name = "app"

urlpatterns = [
    path("posts", PostList.as_view(), name="posts"),
    path("posts/<int:pk>", PostDetail.as_view(), name="post-detail"),
    path("categories", CatAndPosts.as_view(), name="categories"),
]
