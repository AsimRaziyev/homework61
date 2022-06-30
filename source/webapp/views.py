from django.shortcuts import render

from webapp.models import Task


def create_task(request):
    if request.method == "GET":
        return render(request, "create.html")
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
