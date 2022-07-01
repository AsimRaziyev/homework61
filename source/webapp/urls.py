from django.contrib import admin
from django.urls import path

from webapp.views import index_view, create_task, task_view

urlpatterns = [
    path("", index_view),
    path("tasks/add/", create_task),
    path("task/", task_view)
]
