from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('blogs/',views.all_blogs,name='blogs'),

        
    
    path('blogs/<slug:slug>/',views.detailed_blog,name='blog'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('thank-you/',views.thank_you,name='thank_you'),
    path('search/',views.search,name='search'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.signin,name='login'),
    path('logout/',views.signout,name='logout'),

    # API to post a comment
    path('post-comment/',views.post_comment,name='post_comment'),
]