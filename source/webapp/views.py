from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from webapp.models import Task
from webapp.forms import TaskForm




class IndexView(View):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.order_by("-created_at")
        context = {"tasks": tasks}
        return render(request, "index.html", context)


class TaskView(TemplateView):
    template_name = "task_view.html"

    def get_context_data(self, **kwargs):
        pk = kwargs.get("pk")
        task = get_object_or_404(Task, pk=pk)
        kwargs["task"] = task
        return super().get_context_data(**kwargs)


def create_task(request):
    if request.method == "GET":
        form = TaskForm()
        return render(request, "create.html", {"form": form})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            summary = form.cleaned_data.get("summary")
            description = form.cleaned_data.get("description")
            type_text = form.cleaned_data.get("type_text")
            status_text = form.cleaned_data.get("status_text")
            new_task = Task.objects.create(summary=summary, description=description,
                                           type_text=type_text, status_text=status_text)
            return redirect("task_view", pk=new_task.pk)
        return render(request, "create.html", {"form": form})


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
                "type_text": self.task.type_text,
                "status_text": self.task.status_text
            })
            return render(request, "update.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            self.task.summary = form.cleaned_data.get("summary")
            self.task.description = form.cleaned_data.get("description")
            self.task.type_text = form.cleaned_data.get("type_text")
            self.task.status_text = form.cleaned_data.get("status_text")
            self.task.save()
            return redirect("task_view", pk=self.task.pk)
        return render(request, "update.html", {"form": form})
