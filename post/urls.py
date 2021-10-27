from  django.urls import path
from .views import PostListAPIView,PostDetailAPIView

app_name = 'post'

urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name = 'post_list'),
    path('posts/create/', PostListAPIView.as_view(), name = 'post_list'),
    path('posts/<int:id>/', PostDetailAPIView.as_view(), name = 'post_detail'),
]


