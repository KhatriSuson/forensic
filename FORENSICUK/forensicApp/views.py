from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import About, Service, Member, SuccessStory, Feedback, Contact, CarouselItem,Blog
from django.views.generic import View
# Create your views here.

def home(request):
    # Context dictionary to pass data to the template
    views = {}
    
    # Fetch all objects to pass to the template
    views['members'] = Member.objects.all()
    views['blogs'] = SuccessStory.objects.all()
    views['feedbacks'] = Feedback.objects.all()
    views['carousel_items'] = CarouselItem.objects.all()
    views['services'] = Service.objects.all()
    
    # Paginate the 'About' queryset, displaying 2 items per page
    abouts = About.objects.all()
    about_paginator = Paginator(abouts, 2)  # 2 items per page for 'About'
    about_page_number = request.GET.get('about_page')  # Using 'about_page' for pagination
    about_page_obj = about_paginator.get_page(about_page_number)
    views['about_page_obj'] = about_page_obj
    
    # Paginate the 'Service' queryset, displaying 5 items per page
    
    # Handle POST request for contact form submission
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        # Create a new contact entry
        Contact.objects.create(
            name=name,
            email=email,
            message=message
        ).save()
        
        # Optionally redirect to avoid form resubmission on page refresh
        return redirect('home')

    # Render the template with the context
    return render(request, "index.html", views)

    

def about(request):
    abouts = About.objects.all()

    # You can paginate the abouts queryset here as well for the "About Us" page
    paginator = Paginator(abouts, 3)  # Customize the number of items as needed
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'about.html', context)

def about_detail(reqeust, pk):
    about = get_object_or_404(About, pk=pk)
    return render(reqeust, 'about_detail.html', {'about':about})

def services_view(request):
   
    return render(request, 'service.html')



# def services_view(request):
#     # Assuming `services` is a QuerySet of service objects
#     services = Service.objects.all()

#     # Set up pagination
#     paginator = Paginator(services, 2)  # Show 6 services per page
#     page_number = request.GET.get('page')  # Get the page number from the URL
#     page_obj = paginator.get_page(page_number)  # Get the relevant page
#     return render(request, 'service.html', {'page_obj': page_obj})


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


def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    paginator = Paginator(blogs, 2)  # Customize the number of items as needed
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog_list.html', context)
    

def blog_detail(reqeust, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(reqeust, 'blog_detail.html', {'blog':blog})


def test(request):
    views = {}
    views['abouts'] = About.objects.all()
    return render(request, 'home/test_paginator.html', views)




