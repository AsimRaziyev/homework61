from django.contrib import admin
from django.urls import path

from webapp.views import IndexView, RedirectView, CreateProjectView, \
    TaskView, UpdateTask, delete_task, CreateCommentView, \
    ProjectsView, ProjectDetail, CreateTaskWithProject, UpdateComment

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path('tasks/', RedirectView.as_view(pattern_name="index")),
    path('tasks/add/<int:pk>/', CreateTaskWithProject.as_view(), name='create_task'),
    path("task/<int:pk>/", TaskView.as_view(), name="task_view"),
    path('task/<int:pk>/update/', UpdateTask.as_view(), name="update_task"),
    path('task/<int:pk>/delete/', delete_task, name="delete_task"),
    path("task/<int:pk>/comment/add/", CreateCommentView.as_view(), name="task_comment_create"),
    path('comments/<int:pk>/update/', UpdateComment.as_view(), name="update_comment"),

    path('projects/', ProjectsView.as_view(), name="projects_index"),
    path('project/<int:pk>/', ProjectDetail.as_view(), name="project_view"),
    path('project/', CreateProjectView.as_view(), name="project_create")

]
