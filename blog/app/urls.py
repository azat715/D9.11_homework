from django.urls import path

from app.views import PostDetail, PostList


app_name = 'app'

urlpatterns = [  
    path('posts', PostList.as_view(), name='posts'),  
    path('posts/<int:pk>', PostDetail.as_view(), name='post-detail'),
    # path('categories', name='categories')
]