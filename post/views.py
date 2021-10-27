from django.core.exceptions import ValidationError
from django.http import request
from django.shortcuts import render
from rest_framework import generics, permissions, serializers
from rest_framework import status
from rest_framework.response import Response
from .serializers import CreatePostSerializer, LikeSerializer
from .models import Likes, Post
from .permissions import IsAuthorOrReadOnly
from .filters import PostFilter
from django.shortcuts import get_object_or_404
from django.http import Http404,JsonResponse

# Create your views here.

class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = CreatePostSerializer
    queryset = Post.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    
    
    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)
    

class PostListAPIView(generics.ListAPIView):
    serializer_class = CreatePostSerializer
    queryset = Post.objects.all()
    filter_class = PostFilter

    ordering_fields = (
        'created_at',
        'total_likes',
        
    )
    
    filter_fields = (
        'author',
        
    )
      

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView): 
    serializer_class = CreatePostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthorOrReadOnly, )
    lookup_url_kwarg = 'id'
    
class LikeListAPIView(generics.ListAPIView): 
    serializer_class = LikeSerializer
    queryset = Likes.objects.all()

    
class LikeCreateAPIVIew(generics.CreateAPIView): 
    serializer_class = LikeSerializer
    queryset = Likes.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    
    def perform_create(self, serializer):  
        like = serializer.save(author=self.request.user)
        post_id = like.post.id 
        post = Post.objects.get(id = post_id)
        post.likes.add(like)
        post.save()
        
        
            
class LikeDestroyAPIView(generics.DestroyAPIView): 
    serializer_class = LikeSerializer
    queryset = Likes.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    
    def get_object(self):
            return get_object_or_404(Likes, author=self.request.user, post=self.kwargs['post_id'])
        
    def destroy(self, request, *args, **kwargs):
        try: 
            post_id = self.kwargs['post_id']
            post = Post.objects.get(id=post_id)
            instance = self.get_object()
            self.perform_destroy(instance)
            post.save()
        except Http404: 
            pass
        return Response(status=status.HTTP_204_NO_CONTENT, data={"msg": "Deleted"})
         
        
    

            
    
