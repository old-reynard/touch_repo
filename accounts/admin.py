from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Specialty, Review


User = get_user_model()


class AppUserModelAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'created_at', 'confirmed']
    list_display_links = ['full_name', 'email', 'created_at']
    list_filter = ['last_name', 'admin', 'staff', 'latitude', 'longitude']
    search_fields = ['full_name', 'first_name', 'email']

    class Meta:
        model = User


class SpecialtyModelAdmin(admin.ModelAdmin):
    list_display = ['spec_name', 'spec_description']
    list_display_links = ['spec_name', 'spec_description']
    search_fields = ['spec_name']


class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ['header', 'content', 'created_at', 'updated_at', 'from_whom', 'to_whom']
    list_display_links = ['header', 'content', 'created_at', 'updated_at', 'from_whom', 'to_whom']
    search_fields = ['header', 'content']


admin.site.register(User, AppUserModelAdmin)
admin.site.register(Specialty, SpecialtyModelAdmin)
admin.site.register(Review, ReviewModelAdmin)
