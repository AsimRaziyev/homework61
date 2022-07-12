from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, RedirectView
from webapp.models import Task
from webapp.forms import TaskForm, SearchForm


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


def create_task(request):
    if request.method == "POST":
        create_task_form = TaskForm(data=request.POST)
        if create_task_form.is_valid():
            summary = create_task_form.cleaned_data.get("summary")
            description = create_task_form.cleaned_data.get("description")
            type = create_task_form.cleaned_data.get("type")
            status = create_task_form.cleaned_data.get("status")
            new_task = Task.objects.create(summary=summary, description=description, type=type,
                                           status=status)
            return redirect("task_view", pk=new_task.pk)
        return index_view_partial(request, create_task_form, status=400)


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        pass
        return render(request, "delete.html", {"task": task})
    else:
        task.delete()
        return redirect("index")


class UpdateTask(View):

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        self.task = get_object_or_404(Task, pk=pk)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            form = TaskForm(initial={
                "summary": self.task.summary,
                "description": self.task.description,
                "type": self.task.type,
                "status": self.task.status
            })
            return render(request, "update.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            self.task.summary = form.cleaned_data.get("summary")
            self.task.description = form.cleaned_data.get("description")
            self.task.type = form.cleaned_data.get("type")
            self.task.status = form.cleaned_data.get("status")
            self.task.save()
            return redirect("task_view", pk=self.task.pk)
        return render(request, "update.html", {"form": form})
