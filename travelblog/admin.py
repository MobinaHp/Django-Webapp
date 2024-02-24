from django.contrib import admin
from .models import Blog, TravelReview, Review, UserProfile


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'destination', 'rate', 'blog_content']