from django.contrib import admin
from .models import Blog,Comment

# Register your models here.

class CommentInline(admin.StackedInline):
    model = Comment

class AdminBlog(admin.ModelAdmin):
    inlines = [CommentInline,]    

admin.site.register(Blog,AdminBlog)
