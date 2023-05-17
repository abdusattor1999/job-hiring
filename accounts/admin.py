from django.contrib import admin
from .models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age', 'degree', 'kasbi', 'is_busy']
    list_filter = ['first_name', 'is_busy', 'age', 'degree']
    search_fields = ['about', 'degree', 'kasbi']

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'topic']
    search_fields = ['name', 'address', 'topic']
    list_filter = ['name', 'topic']

admin.site.register(Qualification)