from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateField()
    date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return '%s - %s' % (self.id_user, self.id_post.title)


class Like(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.BooleanField()
