# coding=utf-8
from django.contrib import admin

from main.models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("author", "created_at")
