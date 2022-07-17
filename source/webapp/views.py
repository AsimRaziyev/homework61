from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, RedirectView, FormView
from webapp.models import Task
from webapp.forms import TaskForm, SearchForm
from webapp.base_view import FormView as CustomFormView


class IndexView(View):
    def get(self, request, *args, **kwargs):
        create_task_form = TaskForm()
        return index_view_partial(request, create_task_form, status=200)


class MyRedirectView(RedirectView):
    url = "https://www.google.ru/"


class TaskView(TemplateView):
    template_name = "task_view.html"

    def get_context_data(self, **kwargs):
        pk = kwargs.get("pk")
        task = get_object_or_404(Task, pk=pk)
        kwargs["task"] = task
        return super().get_context_data(**kwargs)


def index_view_partial(request, create_task_form, status):
    search_form = SearchForm(data=request.GET)
    tasks = Task.objects.all()
    if search_form.is_valid():
        search_value = search_form.cleaned_data.get("search")
        tasks = tasks.filter(summary__contains=search_value)
    tasks = tasks.order_by("-updated_at")
    context = {"tasks": tasks, "search_form": search_form, "create_task_form": create_task_form}
    return render(request, "index.html", context, status=status)


class CreateTask(CustomFormView):
    form_class = TaskForm
    template_name = "create.html"

    def form_valid(self, form):
        self.task = form.save()
        return super().form_valid(form)

    def get_redirect_url(self):
        return redirect("task_view", pk=self.task.pk)


class UpdateTask(FormView):
    form_class = TaskForm
    template_name = "update.html"

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_objects()
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("task_view", kwargs={"pk": self.task.pk})

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs['instance'] = self.task
        return form_kwargs

    def form_valid(self, form):
        self.task = form.save()
        return super().form_valid(form)

    def get_objects(self):
        return get_object_or_404(Task, pk=self.kwargs.get("pk"))


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        pass
        return render(request, "delete.html", {"task": task})
    else:
        task.delete()
        return redirect("index")