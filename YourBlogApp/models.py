from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.TextField(max_length=50),
    description = models.TextField(max_length=150),
    email = models.EmailField(),
    contact = models.IntegerField()
    


class Editor (models.Model):
    name = models.TextField(max_length=50),
    email = models.EmailField(),
    bio = models.TextField(max_length=250)
    


class Post(models.Model):
    BlogID = models.IntegerField(),
    title = models.TextField(max_length=100),
    subtitle = models.TextField(max_length=150),
    context = models.TextField(max_length=450),
    createdAt = models.DateTimeField(auto_now=True),
    editorID = models.IntegerField(),
    editedAt = models.DateTimeField(auto_now=True)


