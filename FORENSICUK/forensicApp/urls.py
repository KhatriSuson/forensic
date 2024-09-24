from django.urls import path
from forensicApp import views


urlpatterns = [
    path('', views.home, name="home" ),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name="contact"),
    path('test/', views.test, name='test'),
]