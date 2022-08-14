from django.contrib import admin
from django.urls import path

from webapp.views import IndexView, RedirectView, CreateProjectView, \
    TaskView, UpdateTask, DeleteTask, ProjectsView, ProjectDetail,\
    CreateTaskWithProject, UpdateProject, DeleteProject, CreateUserProject, DeleteUserProject

app_name = "webapp"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path('tasks/', RedirectView.as_view(pattern_name="index")),
    path('tasks/add/<int:pk>/', CreateTaskWithProject.as_view(), name='create_task'),
    path("task/<int:pk>/", TaskView.as_view(), name="task_view"),
    path('task/<int:pk>/update/', UpdateTask.as_view(), name="update_task"),
    path('task/<int:pk>/delete/', DeleteTask.as_view(), name="delete_task"),


    path('projects/', ProjectsView.as_view(), name="projects_index"),
    path('project/<int:pk>/', ProjectDetail.as_view(), name="project_view"),
    path('project/', CreateProjectView.as_view(), name="project_create"),
    path('projects/<int:pk>/update/', UpdateProject.as_view(), name="update_project"),
    path('projects/<int:pk>/delete/', DeleteProject.as_view(), name="delete_project"),
    path("project/user_add/<int:pk>/", CreateUserProject.as_view(), name="project_user_create"),
    path("project/user_delete/proekt_id/<int:proekt_pk>/user_id/<int:user_pk>/", DeleteUserProject.as_view(), name="delete_user_project"),

]
