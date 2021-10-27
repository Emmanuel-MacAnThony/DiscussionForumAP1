from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class TimeStampedModel(models.Model): 
    """
    An abstract base class model that provides selfupdating
    ``created`` and ``modified`` fields.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta: 
        abstract = True
        
class Post(TimeStampedModel): 
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
   
    
    def __str__(self) -> str:
        return self.title
    
    @property
    def total_likes(self) -> int:
        return self.likes.all().count()
    
class Likes(TimeStampedModel): 
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    status = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return str(self.author)