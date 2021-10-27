from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Post

@receiver(pre_save, sender=Post)
def post_likes_changed(sender, instance, **kwargs): 
    instance.total_likes = instance.likes.count()
    
