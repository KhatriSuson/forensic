from django.shortcuts import render
from .models import About, Slider, Service, Member
# Create your views here.

def home(request):
    abouts = About.objects.all()
    services = Service.objects.all()
    members = Member.objects.all()
    return render(request, "index.html", {'abouts': abouts, 'services':services, 'members': members})

def about(request):
    abouts = About.objects.all()
    return render(request, 'about.html',{'abouts' : abouts})

def service(request):
    
    return render(request, 'service.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, "contact.html")

def test(request):
    return render(request, 'testindex.html')