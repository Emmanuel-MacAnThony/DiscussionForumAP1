from django.db.models import fields
from rest_framework import serializers
from .models import Post, Likes
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueTogetherValidator

User = get_user_model()



class CreatePostSerializer(serializers.ModelSerializer): 
    created_at = serializers.ReadOnlyField()
    modified_at = serializers.ReadOnlyField()
    likes = serializers.StringRelatedField(many=True,read_only=True)
    author = serializers.StringRelatedField(many=False)
    total_likes = serializers.IntegerField(read_only=True)
    
    class Meta: 
        model = Post
        fields = ('id','title','body','author','created_at','modified_at','likes', 'total_likes', 'description')
        

class LikeSerializer(serializers.ModelSerializer): 
    author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    
    class Meta: 
        model = Likes
        fields = ('id', 'author', 'post')
        validators = [
            UniqueTogetherValidator(
                queryset=Likes.objects.all(),
                fields=['author', 'post']
            )
        ]
        
        
        