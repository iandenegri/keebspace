from django.contrib import admin
from .models import Build

# Register your models here.

@admin.register(Build)
class BuildAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'created_date', 'modified_date']
    search_fields = [
        'name',
        'owner'
    ]
    list_filter = []