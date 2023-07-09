from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from tinymce.models import HTMLField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField()
    date = models.DateTimeField(auto_now_add=True)
    views=models.IntegerField(default=0)
    slug=models.SlugField(default="",null=False,unique=True)

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    message=models.TextField()  

    def __str__(self):
        return self.name
    
class BlogComment(models.Model):
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:50]+"..." + " by " + self.user.username