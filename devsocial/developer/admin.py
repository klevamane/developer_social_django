from django.contrib import admin
from .models import Developer

# Register your models here.


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'created_at', 'updated_at')
    list_display_links = ('email', 'created_at', 'updated_at')
    list_filter = ('created_at', 'email', 'firstname', 'lastname')
    search_fields = ('firstname', 'lastname', 'email')
