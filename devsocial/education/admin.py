from django.contrib import admin
from .models import Education

# Register your models here.


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'school', 'course', 'developer', '_from', 'to', 'created_on')
    list_display_links = ('id', 'school', 'course', 'developer')
    list_filter = ('developer', 'school')
    search_fields = ('developer', 'school')