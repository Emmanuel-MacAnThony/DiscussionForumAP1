from django.contrib import admin
from .models import Post, Likes

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin): 
    list_display =  ('title', 'author')
    
@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin): 
    list_display = ('id',)