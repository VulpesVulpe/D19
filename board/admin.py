from django.contrib import admin
from .models import Category, Post
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
