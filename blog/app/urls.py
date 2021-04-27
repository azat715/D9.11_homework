from app.views import CatAndPosts, PostDetail, PostList
from django.urls import path
from rest_framework.routers import DefaultRouter

app_name = "app"

router = DefaultRouter()
router.register(r'categories', CatAndPosts, basename="cat")

urlpatterns = [
    path("posts", PostList.as_view(), name="posts",),
    path("posts/<int:pk>", PostDetail.as_view(), name="post-detail"),
    # path("categories", CatAndPosts.as_view({'get': 'list'}), name="categories"),
    # path("categories", CatAndPosts.as_view({'post': 'create'}), name="categories"),
    # path("categories/<int:pk>", pass, name="categories-detail"),
]

urlpatterns += router.urls