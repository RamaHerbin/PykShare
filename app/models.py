from django.contrib.auth.models import User
from django.db import models


class Person(User):
    person_id = models.AutoField(primary_key=True)
    birth_date = models.DateField(default=1990)
    full_name = models.CharField(max_length=200, null=True, blank=False)


class Picture(models.Model):
    picture_id = models.AutoField(primary_key=True)
    image = models.ImageField(default='')
    uploader = models.ForeignKey(Person, on_delete=models.CASCADE)
    libelle = models.CharField(max_length=200, null=False, blank=False)


class Comment(models.Model):
    id_user = models.ForeignKey(Person, on_delete=models.CASCADE)
    id_photo = models.ForeignKey(Picture, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=200)


class Like(models.Model):
    id_user = models.ForeignKey(Person, on_delete=models.CASCADE)
    id_photo = models.ForeignKey(Picture, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    value = models.BooleanField()


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    uploaded_at = models.DateField()
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    like = models.ForeignKey(Like, on_delete=models.CASCADE)
