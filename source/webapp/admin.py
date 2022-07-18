from django.contrib import admin

# Register your models here.
from webapp.models import Task, Statuses, Comment, Types, Tag




class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'author', 'description', 'created_at']
    list_display_links = ['description']
    list_filter = ['summary']
    search_fields = ['description', 'summary']
    fields = ['summary', 'author', 'description', 'updated_at']
    readonly_fields = ['updated_at']


admin.site.register(Task, TaskAdmin)


class StatusesAdmin(admin.ModelAdmin):
    list_display = ['id', 'status_text', 'created_at']


admin.site.register(Statuses, StatusesAdmin)


class TypesAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_text', 'created_at']


admin.site.register(Types, TypesAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'author', 'created_at']


admin.site.register(Comment, CommentAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']


admin.site.register(Tag, TagAdmin)
