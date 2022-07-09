from django.contrib import admin

# Register your models here.
from webapp.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'task_name', 'created_at']
    list_display_links = ['description']
    list_filter = ['status']
    search_fields = ['description', 'task_name']
    fields = ['description', 'status', 'task_name', 'updated_at']
    readonly_fields = ['updated_at']


admin.site.register(Task, TaskAdmin)
