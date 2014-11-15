from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Subforum(models.Model):
    name = models.CharField(max_length=16)

class Department(Subforum):
    colloquiums = models.TextField()

class Class(Subforum):
    department = models.ForeignKey(Department)
    office_hours = models.TextField()
    mentor_sessions = models.TextField()

class User(AbstractBaseUser):
    email = models.CharField(max_length=64, unique=True)
    display_name = models.CharField(max_length=64)
    
    forums = models.ManyToManyField(Subforum)
    
    USERNAME_FIELD = 'email'

class Tag(models.Model):
    name = models.CharField(max_length=32)
   
class Post(models.Model):
    poster = models.ForeignKey(User)
    content = models.TextField()

class Thread(Post):
    subforum = models.ForeignKey(Subforum)
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=128)

class Comment(Post):
    thread = models.ForeignKey(Thread)

class Reply(Post):
    comment = models.ForeignKey(Comment)
