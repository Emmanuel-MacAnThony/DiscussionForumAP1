"""
A module of customized django filters
"""
from django_filters import rest_framework as filters
from django_filters.filters import AllValuesFilter, DateTimeFilter, NumberFilter
from rest_framework import fields
from .models import Post

class PostFilter(filters.FilterSet): 
    from_creation_date = DateTimeFilter(field_name='created_at', lookup_expr='gte')
    to_creation_date = DateTimeFilter(field_name='created_at', lookup_expr='lte')
    min_likes = NumberFilter(field_name='total_likes', lookup_expr='gte')
    max_likes = NumberFilter(field_name='total_likes', lookup_expr='lte')
    author_name = AllValuesFilter(field_name='author__username') 
    
    class Meta: 
        model = Post
        fields = (
            'from_creation_date',
            'to_creation_date',
            'min_likes',
            'max_likes',
            'author_name'
        )