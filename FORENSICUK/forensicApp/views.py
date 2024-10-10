from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import About, Service, Member, Feedback, Contact, CarouselItem,Blog, BlogPost, Like, Comment
from .forms import CommentForm
# Create your views here.

def home(request):
    # Context dictionary to pass data to the template
    views = {}
    views['members'] = Member.objects.all()
    views['feedbacks'] = Feedback.objects.all()
    views['carousel_items'] = CarouselItem.objects.all()

    # Paginate the abouts queryset, displaying 2 items per page
    abouts = About.objects.all()
    paginator = Paginator(abouts, 2)  # 2 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Add the paginated abouts to the context
    views['page_obj'] = page_obj
    
    services = Service.objects.all()
    paginator = Paginator(services, 3)  # Customize the number of items as needed
    page_number = request.GET.get('page')
    page_obj_service = paginator.get_page(page_number)
    views['page_obj_service'] = page_obj_service
   

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
    services = Service.objects.all()
    paginator = Paginator(services, 6)  # Customize the number of items as needed
    page_number = request.GET.get('page')
    page_obj_service = paginator.get_page(page_number)
    context = {
        'page_obj_service': page_obj_service,
    }
   
    return render(request, 'service.html', context)




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

# blog update view


def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    commnets = post.comments.all()
    is_liked = False
    
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True
        
    if request.method == 'POST':
        commnet_form = CommentForm(request.POst)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'is_liked': is_liked,
        'total_likes': post.total_likes(),
    }
    return render(request, 'blog/post_detail.html', context)

# @login_required
def like_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post_detail', post_id=post.id)
