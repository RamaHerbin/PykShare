from django.contrib import admin
# from comments.models omport Post
from app.models import Comment, Person, Like, Picture, Post

admin.site.register(Comment, admin.ModelAdmin)
admin.site.register(Person, admin.ModelAdmin)
admin.site.register(Like, admin.ModelAdmin)
admin.site.register(Picture, admin.ModelAdmin)
admin.site.register(Post, admin.ModelAdmin)