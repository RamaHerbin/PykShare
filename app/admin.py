from django.contrib import admin
# from comments.models omport Post
from app.models import Comment, Post

admin.site.register(Comment, admin.ModelAdmin)
admin.site.register(Post, admin.ModelAdmin)