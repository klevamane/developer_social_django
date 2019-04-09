from django.contrib import admin
from .models import Experience
# Register your models here.


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'organization', 'location', 'developer')
    list_display = ('id', 'organization', 'location', 'developer', '_from', 'to', 'designation')
    search_fields = ('organization', 'location', 'developer')
