from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import About, Service, Member, Feedback, Contact, CarouselItem,Blog, Subscriber, Newsletter
from django.core.mail import send_mail
from django.conf import settings
from .forms import SubscriberForm
# Create your views here.

# def home(request):
#     # Context dictionary to pass data to the template
#     views = {}
#     views['members'] = Member.objects.all()
#     views['feedbacks'] = Feedback.objects.all()
#     views['carousel_items'] = CarouselItem.objects.all()

#     # Paginate the abouts queryset, displaying 2 items per page
#     abouts = About.objects.all()
#     paginator = Paginator(abouts, 2)  # 2 items per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
    
#     # Add the paginated abouts to the context
#     views['page_obj'] = page_obj
    
#     services = Service.objects.all()
#     paginator = Paginator(services, 3)  # Customize the number of items as needed
#     page_number = request.GET.get('page')
#     page_obj_service = paginator.get_page(page_number)
#     views['page_obj_service'] = page_obj_service
   

#     # Handle POST request for contact form submission
#     if request.method == "POST":
#         name = request.POST['name']
#         email = request.POST['email']
#         message = request.POST['message']
        
#         # Create a new contact entry
#         Contact.objects.create(
#             name=name,
#             email=email,
#             message=message
#         ).save()
        
#         # Optionally redirect to avoid form resubmission on page refresh
#         return redirect('home')

#     # Render the template with the context
#     return render(request, "index.html", views)

    

# def about(request):
#     abouts = About.objects.all()

#     # You can paginate the abouts queryset here as well for the "About Us" page
#     paginator = Paginator(abouts, 3)  # Customize the number of items as needed
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     context = {
#         'page_obj': page_obj,
#     }
#     return render(request, 'about.html', context)

# def about_detail(reqeust, pk):
#     about = get_object_or_404(About, pk=pk)
#     return render(reqeust, 'about_detail.html', {'about':about})

# def services_view(request):
#     services = Service.objects.all()
#     paginator = Paginator(services, 6)  # Customize the number of items as needed
#     page_number = request.GET.get('page')
#     page_obj_service = paginator.get_page(page_number)
#     context = {
#         'page_obj_service': page_obj_service,
#     }
   
#     return render(request, 'service.html', context)

def home(request):
    # Context dictionary to pass data to the template
    context = {}
    context['members'] = Member.objects.all()
    context['feedbacks'] = Feedback.objects.all()
    context['carousel_items'] = CarouselItem.objects.all()

    # Paginate the About objects, displaying 2 items per page
    abouts = About.objects.all()
    paginator_about = Paginator(abouts, 2)
    page_number_about = request.GET.get('about_page')
    page_obj_about = paginator_about.get_page(page_number_about)
    context['page_obj_about'] = page_obj_about
    
    # Paginate the Service objects, displaying 3 items per page
    services = Service.objects.all()
    paginator_service = Paginator(services, 3)
    page_number_service = request.GET.get('service_page')
    page_obj_service = paginator_service.get_page(page_number_service)
    context['page_obj_service'] = page_obj_service
   
    # Initialize and handle POST request for the contact form submission
    if request.method == "POST" and 'contact_form' in request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Create a new contact entry
        Contact.objects.create(name=name, email=email, message=message)
        
        # Redirect to avoid form resubmission on page refresh
        return redirect('home')

    # Initialize the Subscriber form
    form = SubscriberForm()
    if request.method == 'POST' and 'subscriber_form' in request.POST:
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            send_welcome_email(form.cleaned_data['email'])
            return redirect('thank_you')
    
    # Add the Subscriber form to the context
    context['form'] = form

    # Render the template with the context
    return render(request, "index.html", context)


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
    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog_list.html', context)
    

def blog_detail(reqeust, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(reqeust, 'blog_detail.html', {'blog':blog})



# subscribe and newletter

def subscribe(request):
    form = SubscriberForm()
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            send_welcome_email(form.cleaned_data['email'])
            return redirect('thank_you')
    return render(request, 'newsletter/subscribe.html', {'form': form})

def thank_you(request):
    return render(request, 'newsletter/thank_you.html')

# Send Welcome Email
def send_welcome_email(email):
    send_mail(
        'Welcome to Our Newsletter',
        'Thank you for subscribing to our newsletter!',
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )

# Send Newsletter to All Subscribers
def send_newsletter(newsletter_id):
    newsletter = Newsletter.objects.get(id=newsletter_id)
    subscribers = Subscriber.objects.all()

    for subscriber in subscribers:
        send_mail(
            newsletter.subject,
            newsletter.message,
            settings.DEFAULT_FROM_EMAIL,
            [subscriber.email],
            fail_silently=False,
        )


