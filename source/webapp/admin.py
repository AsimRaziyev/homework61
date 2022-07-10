from django.contrib import admin

# Register your models here.
from webapp.models import Task, Status, Comment, Type


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'summary', 'created_at']
    list_display_links = ['description']
    list_filter = ['summary']
    search_fields = ['description', 'summary']
    fields = ['description', 'summary', 'updated_at']
    readonly_fields = ['updated_at']


admin.site.register(Task, TaskAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'status_text', 'created_at']


admin.site.register(Status, StatusAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_text', 'created_at']


admin.site.register(Type, TypeAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'author', 'created_at']


admin.site.register(Comment, CommentAdmin)
