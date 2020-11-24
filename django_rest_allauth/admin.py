from django.contrib import admin
from .models import DjangoRestAllAuth
class DjangoRestAllAuthAdmin(admin.ModelAdmin):
    list_display = ['provider', 'email', 'username', 'social_id']
admin.site.register(DjangoRestAllAuth, DjangoRestAllAuthAdmin)