from django.shortcuts import render
from .models import About, Slider, Service, Member, SuccessStory, Feedback, Contact
from django.views.generic import View
# Create your views here.

def home(request):
    views = {}
    views['abouts'] = About.objects.all()
    views['services'] = Service.objects.all()
    views['members'] = Member.objects.all()
    views['blogs'] = SuccessStory.objects.all()
    views['feedbacks'] = Feedback.objects.all()

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Contact.objects.create(
            name = name,
            email = email,
            message = message
        ).save()
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
    views = {}
    views['blogs'] = SuccessStory.objects.all()
    return render(request, 'blog.html', views)

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Contact.objects.create(
            name = name,
            email = email,
            message = message
        ).save()
    return render(request, "contact.html")

def test(request):
    return render(request, 'testindex.html')