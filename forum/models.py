from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

class Subforum(models.Model):
    name = models.CharField(max_length=16, unique=True)
    full_name = models.CharField(max_length=128)
    
    def get_url(self):
        return '/forums/' + self.name.lower() + '/'

class Department(Subforum):
    colloquiums = models.TextField()

class Class(Subforum):
    department = models.ForeignKey(Department)
    office_hours = models.TextField()
    mentor_sessions = models.TextField()
    
    def get_url(self):
        return self.department.get_url() + self.name.lower() + '/'

class User(AbstractBaseUser):
    email = models.CharField(max_length=64, unique=True)
    display_name = models.CharField(max_length=64)
    
    forums = models.ManyToManyField(Subforum)
    
    USERNAME_FIELD = 'email'
    
    objects = BaseUserManager()
    
    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.display_name

class Tag(models.Model):
    name = models.CharField(max_length=32, unique=True)
   
class Post(models.Model):
    poster = models.ForeignKey(User)
    content = models.TextField()
    date = models.DateTimeField(default = timezone.now)

class Thread(Post):
    subforum = models.ForeignKey(Subforum)
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=128)
    
    def get_url(self):
        if isinstance(self.subforum, Class):
            s = Class.objects.get(name = self.subforum.name).get_url()
        else:
            s = self.subforum.get_url()
        return s + str(self.id) +'/'

class Comment(Post):
    thread = models.ForeignKey(Thread)

class Reply(Post):
    comment = models.ForeignKey(Comment)
