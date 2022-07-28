from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from webapp.models import Project, Task
from webapp.forms import ProjectForm


class ProjectsView(ListView):
    model = Project
    template_name = "projects/index_project.html"
    context_object_name = "projects"
    ordering = "id"
    paginate_by = 20

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProjectDetail(DetailView):
    template_name = "projects/project_view.html"
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.object.tasks.order_by("-created_at")
        return context


class CreateProjectView(CreateView):
    form_class = ProjectForm
    template_name = "projects/create_project.html"
