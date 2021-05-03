from app.views import CatAndPosts, PostDetail, PostList
from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = "app"

schema_view = get_schema_view(
   openapi.Info(
      title="Blog API",
      default_version='v1',
      description="Cool blog on Heroku",
      contact=openapi.Contact(email="azat715@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()
router.register(r'categories', CatAndPosts, basename="cat")

urlpatterns = [
    path("posts", PostList.as_view(), name="posts",),
    path("posts/<int:pk>", PostDetail.as_view(), name="post-detail"),
    # path("categories", CatAndPosts.as_view({'get': 'list'}), name="categories"),
    # path("categories", CatAndPosts.as_view({'post': 'create'}), name="categories"),
    # path("categories/<int:pk>", pass, name="categories-detail"),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns += router.urls