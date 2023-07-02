from django.shortcuts import render,redirect
from .models import Blog,Contact



# Create your views here.
def home(request):
    blogs=Blog.objects.all().order_by('-date')[:8]
    return render(request, 'blog/home.html',{
        'blogs':blogs
    })

def detailed_blog(request,slug):
    blog=Blog.objects.get(slug=slug)
    return render(request, 'blog/blog.html',{
        'blog':blog
    })

def all_blogs(request):
    blogs=Blog.objects.all().order_by('-date')
    return render(request, 'blog/all_blogs.html',{
        'blogs':blogs
    })

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        message=request.POST.get("message")

        Contact.objects.create(name=name,email=email,message=message)
        return redirect('thank_you')
        
    return render(request, 'blog/contact.html')

def thank_you(request):
    return render(request, 'blog/thank_you.html')