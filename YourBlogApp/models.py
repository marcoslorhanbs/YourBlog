from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=150)
    email = models.EmailField()
    category = models.TextField(max_length=20)
    #future feature: add subcategories field to appear like sections in the blog.
    


class Editor (models.Model):
    name = models.TextField(max_length=50)
    bio = models.TextField(max_length=250)
    


class Post(models.Model):
    BlogID = models.IntegerField()
    title = models.TextField(max_length=100)
    subtitle = models.TextField(max_length=150)
    context = models.TextField(max_length=450)
    createdAt = models.DateTimeField(auto_now=True)
    editorID = models.IntegerField()
    editedAt = models.DateTimeField(auto_now=True)
    #future feature: add a new field subcategory to make the posts from that subcategory appear in that speci-
    #-fic category


