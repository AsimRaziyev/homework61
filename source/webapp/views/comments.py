from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView
from webapp.forms import CommentForm
from webapp.models import Task


class CreateCommentView(CreateView):
    form_class = CommentForm
    template_name = "comments/create.html"

    def form_valid(self, form):
        task = get_object_or_404(Task, pk=self.kwargs.get("pk"))
        form.instance.task = task
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("task_view", kwargs={"pk": self.object.task.pk})
