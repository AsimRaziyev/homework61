from django.shortcuts import render


def index_view(request):
    query = request.GET.getlist("name", "ttttt")
    print(query)
    context = {"name": query, "test": "lalala"}
    return render(request, "index.html", context)


def create_task(request):
    if request.method == "GET":
        return render(request, "create.html")
    else:
        context = {
            "description": request.POST.get("description"),
            "status": request.POST.get("status"),
        }
        return render(request, 'task_view.html', context)