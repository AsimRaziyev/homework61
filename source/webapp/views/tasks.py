from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import RedirectView, ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Task, Project
from webapp.forms import TaskForm, SearchForm, TaskFormProject


class IndexView(ListView):
    model = Task
    template_name = "tasks/index.html"
    context_object_name = "tasks"
    ordering = "-updated_at"
    paginate_by = 9

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        self.sort_value = self.get_sort_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        tasks = Task.objects.all()
        if self.search_value:
            tasks = tasks.filter(Q(author__icontains=self.search_value) | Q(summary__icontains=self.search_value))
        if self.sort_value:
            tasks = tasks.order_by(self.sort_value)
        return tasks

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["form"] = self.form
        if self.search_value:
            query = urlencode({'search': self.search_value})
            context["query"] = query
            context["search"] = self.search_value
        return context

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get("search")

    def get_sort_value(self):
        return self.request.GET.get("sort")


class MyRedirectView(RedirectView):
    url = "https://www.google.ru/"


class TaskView(DetailView):
    template_name = "tasks/task_view.html"
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.order_by("-created_at")
        return context


class CreateTaskWithProject(CreateView):
    form_class = TaskFormProject
    template_name = "tasks/create_tasks_project.html"

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get("pk"))
        form.instance.project = project
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("project_view", kwargs={"pk": self.object.project.pk})


class UpdateTask(UpdateView):
    form_class = TaskForm
    template_name = "tasks/update.html"
    model = Task


class DeleteTask(DeleteView):
    model = Task
    template_name = "tasks/delete.html"
    success_url = reverse_lazy('index')

