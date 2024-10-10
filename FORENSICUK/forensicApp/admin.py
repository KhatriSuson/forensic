from django.contrib import admin
from .models import About, Service, Member, Feedback, Contact, CarouselItem, Blog, BlogPost
# Register your models here.
admin.site.register(About)
admin.site.register(Service)
admin.site.register(Member)
admin.site.register(Feedback)
admin.site.register(Contact)
admin.site.register(CarouselItem)

admin.site.register(BlogPost)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)
