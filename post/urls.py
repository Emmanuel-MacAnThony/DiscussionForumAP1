from  django.urls import path
from .views import PostListAPIView,PostDetailAPIView,LikeCreateAPIVIew, PostCreateAPIView, LikeDestroyAPIView

app_name = 'post'

urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name = 'post_list'),
    path('posts/create/', PostCreateAPIView.as_view(), name = 'post_list'),
    path('posts/like/', LikeCreateAPIVIew.as_view(), name='like_create'),
    path('posts/like/<int:post_id>/', LikeDestroyAPIView.as_view(), name='like_detail'),
    path('posts/<int:id>/', PostDetailAPIView.as_view(), name = 'post_detail'),
]


