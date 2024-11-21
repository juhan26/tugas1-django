from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('my-projects/', views.my_projects, name='my_projects'),
    path('guest-book/', views.guest_book, name='guest_book'),
    path('blog/', views.blog, name='blog'),
]