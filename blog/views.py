from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Blog,Contact
from django.db.models import Q



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

        # Set a session variable to indicate that the form has been submitted
        request.session['submitted'] = True
        # Redirect to the thank you page
        return redirect('thank_you')
        
    return render(request, 'blog/contact.html')

def thank_you(request):
    # Check if the session variable is set to True
    if not request.session.get('submitted',False):
        # If it is not, redirect to the contact page
        messages.error(request, 'Please fill out the form first.')
        return redirect('contact')
    
    # Clear the session variable
    request.session['submitted'] = False

    return render(request, 'blog/thank_you.html')

def search(request):
    # Get the search query from the GET request and strip any leading/trailing whitespace
    query = request.GET.get('query').strip()
    if not query:
        # If the search query is empty, redirect to the home page and display an error message
        messages.error(request, 'Please enter a search query.')
        return redirect('home')
    
    # Search for blog posts that contain the search query in the title or description
    searched_blogs = Blog.objects.filter(Q(title__contains=query) | Q(description__contains=query))
    context = {
        'searched_blogs': searched_blogs,
        'query': query
    }
    # Render the search results page
    return render(request, 'blog/search.html', context)


    