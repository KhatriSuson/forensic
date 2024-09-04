from django.urls import path
from forensicApp import views


urlpatterns = [
    path('', views.home, name="home" ),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name="contact"),
]