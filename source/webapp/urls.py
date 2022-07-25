from django.contrib import admin
from django.urls import path

from webapp.views import IndexView,  RedirectView, CreateTask, TaskView, UpdateTask, delete_task, CreateCommentView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path('tasks/', RedirectView.as_view(pattern_name="index")),
    path("tasks/add/", CreateTask.as_view(), name="create_task"),
    path("task/<int:pk>/", TaskView.as_view(), name="task_view"),
    path('task/<int:pk>/update', UpdateTask.as_view(), name="update_task"),
    path('task/<int:pk>/delete', delete_task, name="delete_task"),
    path("task/<int:pk>/comment/add/", CreateCommentView.as_view(), name="task_comment_create"),

]
