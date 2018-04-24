from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    fields = ['short_name', 'full_name']

admin.site.register(Project, ProjectAdmin)
