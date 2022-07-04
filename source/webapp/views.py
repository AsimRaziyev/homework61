from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task
from webapp.models import STATUS_CHOICES
from webapp.forms import TaskForm


def index_view(request):
    tasks = Task.objects.order_by("-created_at")
    context = {"tasks": tasks}
    return render(request, "index.html", context)


def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_view.html', {"task": task})


def create_task(request):
    if request.method == "GET":
        return render(request, "create.html", {"statuses": STATUS_CHOICES})
    else:
        description = request.POST.get("description")
        status = request.POST.get("status")
        created_at = request.POST.get("created_at")
        if created_at == "":
            created_at = None
        else:
            created_at = created_at
    new_task = Task.objects.create(description=description, status=status, created_at=created_at)
    return redirect("task_view", pk=new_task.pk)


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        pass
        return render(request, "delete.html", {"task": task})
    else:
        task.delete()
        return redirect("index")


def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        form = TaskForm(initial={
            "description": task.description,
            "status": task.status,
            "created_at": task.created_at
        })
        return render(request, "update.html", {"form": form})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.description = form.cleaned_data.get("description")
            task.status = form.cleaned_data.get("status")
            task.created_at = form.cleaned_data.get("created_at")
            task.save()
            return redirect("index")
        return render(request, "update.html", {"form": form})
