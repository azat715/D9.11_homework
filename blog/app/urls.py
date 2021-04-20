from django.urls import path

from app.views import PostDetail, PostList


app_name = 'app'

urlpatterns = [  
    path('', PostList.as_view(), name='post-list'),  
    path('<int:pk>', PostDetail.as_view(), name='post-detail'),  
]