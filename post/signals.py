from django.db.models.signals import pre_save,post_delete
from django.dispatch import receiver
from .models import Post, Likes

@receiver(pre_save, sender=Post)
def post_likes_changed(sender, instance, **kwargs): 
    instance.total_likes = instance.likes.count()
    
