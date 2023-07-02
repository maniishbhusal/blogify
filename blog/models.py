from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(default="",null=False,unique=True)

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    message=models.TextField()

    def __str__(self):
        return self.name