from django.db.models import fields
from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model

User = get_user_model()



class CreatePostSerializer(serializers.ModelSerializer): 
    created_at = serializers.ReadOnlyField()
    modified_at = serializers.ReadOnlyField()
    likes = serializers.StringRelatedField(many=True,read_only=True)
    author = serializers.StringRelatedField(many=False)
    
    class Meta: 
        model = Post
        fields = ('id','title','body','author','created_at','modified_at','likes')
        
        
        