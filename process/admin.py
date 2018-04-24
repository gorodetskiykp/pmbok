from django.contrib import admin
from .models import Process, ProcessGroup, KnowlegeField

class ProcessAdmin(admin.ModelAdmin):
    list_display = ['name', 'process_group', 'knowlege_field']
    ordering = ['process_group', 'knowlege_field', 'order']

admin.site.register(Process, ProcessAdmin)
admin.site.register(ProcessGroup)
admin.site.register(KnowlegeField)
