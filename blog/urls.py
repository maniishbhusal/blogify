from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('blogs/',views.all_blogs,name='blogs'),
    path('blogs/<slug:slug>/',views.detailed_blog,name='blog'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('thank-you/',views.thank_you,name='thank_you')
]