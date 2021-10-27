from django.http import request
from django.shortcuts import render
from rest_framework import generics, permissions, serializers
from .serializers import CreatePostSerializer, LikeSerializer
from .models import Likes, Post
from .permissions import IsAuthorOrReadOnly
from .filters import PostFilter

# Create your views here.

class PostListAPIView(generics.ListCreateAPIView):
    serializer_class = CreatePostSerializer
    queryset = Post.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_class = PostFilter

    ordering_fields = (
        'created_at',
        'total_likes',
        
    )
    
    filter_fields = (
        'author',
        
    )
    
    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)
    

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView): 
    serializer_class = CreatePostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthorOrReadOnly, )
    lookup_field = 'id'
    
class LikeCreateAPIVIew(generics.CreateAPIView): 
    serializer_class = LikeSerializer
    queryset = Likes.objects.all()
    
    def perform_create(self, serializer):
        if self.request.user.is_anonymous: 
            like =  serializer.save()
            post_id = like.post.id 
            post = Post.objects.get(id = post_id)
            post.likes.add(like)
            post.save()
            
        else: 
            #when user is authenticated, associate like with authenticated user
            like = serializer.save(author=self.request.user)
            post_id = like.post.id 
            post = Post.objects.get(id = post_id)
            post.likes.add(like)
            post.save()
            
    
