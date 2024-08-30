from django.urls import path
from forensicApp import views


urlpatterns = [
    path('', views.home, name="home" ),
]