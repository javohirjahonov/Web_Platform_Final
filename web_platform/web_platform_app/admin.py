from django.contrib import admin
from .models import ServiceModel, OurTeamModel, ContactModel, CountersModel, PostModel


class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']


class PostsModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']


class OurTeamModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'created_at']
    search_fields = ['name', 'position']
    list_filter = ['created_at']


class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'created_at']
    search_fields = ['name', 'phone', 'email']
    list_filter = ['created_at']


class CountersAdmin(admin.ModelAdmin):
    list_display = ['title', 'count']
    search_fields = ['title', 'count']


admin.site.register(ServiceModel, ServiceModelAdmin)
admin.site.register(OurTeamModel, OurTeamModelAdmin)
admin.site.register(ContactModel, ContactModelAdmin)
admin.site.register(CountersModel, CountersAdmin)
admin.site.register(PostModel, PostsModelAdmin)