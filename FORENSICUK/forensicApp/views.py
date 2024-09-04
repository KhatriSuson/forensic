from django.shortcuts import render
from .models import About, Slider, Service, Member
from django.views.generic import View
# Create your views here.

def home(request):
    views = {}
    views['abouts'] = About.objects.all()
    views['services'] = Service.objects.all()
    views['members'] = Member.objects.all()
    return render(request, "index.html",views)

def about(request):
    views = {}
    views['abouts'] = About.objects.all()
    return render(request, 'about.html',views)

def service(request):
    views = {}
    views['services'] = Service.objects.all()
    views['members'] = Member.objects.all()
    return render(request, 'service.html', views)

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, "contact.html")

def test(request):
    return render(request, 'testindex.html')