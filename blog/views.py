from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Blog, Contact
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    blogs = Blog.objects.all().order_by('-date')[:8]
    return render(request, 'blog/home.html', {
        'blogs': blogs
    })


def detailed_blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'blog/blog.html', {
        'blog': blog
    })


def all_blogs(request):
    blogs = Blog.objects.all().order_by('-date')
    return render(request, 'blog/all_blogs.html', {
        'blogs': blogs
    })


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Contact.objects.create(name=name, email=email, message=message)

        # Set a session variable to indicate that the form has been submitted
        request.session['submitted'] = True
        # Redirect to the thank you page
        return redirect('thank_you')

    return render(request, 'blog/contact.html')


def thank_you(request):
    # Check if the session variable is set to True
    if not request.session.get('submitted', False):
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
    searched_blogs = Blog.objects.filter(
        Q(title__contains=query) | Q(description__contains=query))
    context = {
        'searched_blogs': searched_blogs,
        'query': query
    }
    # Render the search results page
    return render(request, 'blog/search.html', context)

def signup(request):
    if request.method == "POST":
        # Get the form data submitted by the user
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Check if a user with the same username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('signup')

        # Check if a user with the same email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('signin')

        # Create a new user if the passwords match and the username and email are unique
        if password == confirm_password:
            user = User.objects.create_user(
                username=username, email=email, password=password)
            user.save()
            messages.success(
                request, 'Account created successfully! Login now.')
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('signup')

    return render(request, 'blog/signup.html')


def signin(request):
    if request.method == "POST":
        # Get the form data submitted by the user
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        # Log the user in if the credentials are valid
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('login')

    return render(request, 'blog/login.html')

@login_required(login_url='login')
def signout(request):
    # Log the user out
    logout(request)

    # Display a success message
    messages.success(request, 'Logged out successfully!')

    # Redirect the user to the home page
    return redirect('home')
