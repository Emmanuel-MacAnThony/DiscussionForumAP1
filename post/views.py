from django.shortcuts import render
from rest_framework import generics, permissions, serializers
from .serializers import CreatePostSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly

# Create your views here.

class PostListAPIView(generics.ListCreateAPIView):
    serializer_class = CreatePostSerializer
    queryset = Post.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    
    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)
    

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView): 
    serializer_class = CreatePostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthorOrReadOnly, )
    lookup_field = 'id'
    
