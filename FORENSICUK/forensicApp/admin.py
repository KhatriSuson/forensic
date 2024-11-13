from django.contrib import admin
from .models import About, Service, Member, Feedback, Contact, CarouselItem, Blog, Subscriber, Newsletter
from django.core.mail import send_mail

def send_newsletter(modeladmin, request, queryset):
    # Adjusting the filter based on the field that exists
    subscribers = Subscriber.objects.filter(subscribed_on__isnull=False)  # Assuming 'subscribed_on' is used to mark subscribers
    for subscriber in subscribers:
        # Your logic to send the newsletter
        pass

# Register your models here.
admin.site.register(About)
admin.site.register(Service)
admin.site.register(Member)
admin.site.register(Feedback)
admin.site.register(Contact)
admin.site.register(CarouselItem)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)

@admin.action(description='Send Newsletter')
def send_newsletter(modeladmin, request, queryset):
    subscribers = Subscriber.objects.filter(subscribed=True)
    for newsletter in queryset:
        subject = newsletter.subject
        message = newsletter.message
        recipient_list = [subscriber.email for subscriber in subscribers]
        send_mail(subject, message, 'your-email@gmail.com', recipient_list)

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['subject', 'created_at']
    actions = [send_newsletter]

admin.site.register(Subscriber)
admin.site.register(Newsletter, NewsletterAdmin)