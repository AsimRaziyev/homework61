from django.contrib import admin

# Register your models here.
from webapp.models import Task, Statuses, Types, Tag, Project


class TagInline(admin.TabularInline):
    model = Task.tags.through


class TypesInline(admin.TabularInline):
    model = Task.types.through


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'author', 'description', 'created_at']
    list_display_links = ['summary', 'description']
    list_filter = ['summary']
    search_fields = ['description', 'summary']
    fields = ['summary', 'author', 'description', 'updated_at']
    readonly_fields = ['updated_at']
    # filter_horizontal = ["tags"]
    inlines = [TagInline, TypesInline]


admin.site.register(Task, TaskAdmin)


class StatusesAdmin(admin.ModelAdmin):
    list_display = ['id', 'status_text', 'created_at']
    list_display_links = ['status_text']


admin.site.register(Statuses, StatusesAdmin)


class TypesAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_text', 'created_at']
    list_display_links = ['type_text']
    inlines = [TypesInline]


admin.site.register(Types, TypesAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    list_display_links = ['name']
    inlines = [TagInline]


admin.site.register(Tag, TagAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'start_date', 'end_date']
    list_display_links = ['name']



admin.site.register(Project, ProjectAdmin)
