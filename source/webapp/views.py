from django.shortcuts import render
from webapp.models import Task
from webapp.models import STATUS_CHOICES


def index_view(request):
    tasks = Task.objects.order_by("-created_at")
    context = {"tasks": tasks}
    return render(request, "index.html", context)


def task_view(request):
    pk = request.GET.get("pk")
    task = Task.objects.get(pk=pk)
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
    context = {"task": new_task}
    return render(request, 'task_view.html', context)
