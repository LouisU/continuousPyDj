from django.contrib import admin
from .models import *
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'phone', 'email', 'password')
    list_filter = ('username', 'name', 'phone', 'email')


# admin.site.register(UserProfile) # Use the default options
admin.site.register(UserProfile, UserProfileAdmin) # use the customized options