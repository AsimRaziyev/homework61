from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Project, Task
from webapp.forms import ProjectForm


class ProjectsView(ListView):
    model = Project
    template_name = "projects/index_list_project.html"
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


class CreateProjectView(PermissionRequiredMixin, CreateView):
    form_class = ProjectForm
    template_name = "projects/create_project.html"

    def has_permission(self, **kwargs):
        return self.request.user.has_perm("webapp.add_project")


class UpdateProject(PermissionRequiredMixin, UpdateView):
    form_class = ProjectForm
    template_name = "projects/update_project.html"
    model = Project

    def get_success_url(self):
        return reverse("webapp:project_view", kwargs={"pk": self.object.pk})

    def has_permission(self, **kwargs):
        return self.request.user.has_perm("webapp.change_project")


class DeleteProject(PermissionRequiredMixin, DeleteView):
    model = Project
    context_object_name = 'project'
    template_name = "projects/delete_project.html"
    success_url = reverse_lazy('webapp:projects_index')

    def has_permission(self, **kwargs):
        return self.request.user.has_perm("webapp.delete_project")


class CreateUserProject(PermissionRequiredMixin, CreateView):

    def get(self, request, *args, **kwargs):
        proekt = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        context = {
            'proekt': proekt,
            'users': User.objects.all()
        }
        return render(request, 'projects/create_user.html', context)

    def post(self, request, *args, **kwargs):
        proekt = get_object_or_404(Project, pk=request.POST.get('project_user'))
        user = int(request.POST.get('user_project'))
        proekt.users.add(user)
        return redirect('webapp:project_view', pk=proekt.pk)

    def has_permission(self, **kwargs):
        return self.request.user.has_perm("webapp.add_users_to_the_project")


class DeleteUserProject(PermissionRequiredMixin, View):
    pk_url_kwarg = 'proekt_pk'

    def get(self, request, *args, **kwargs):
        proekt = get_object_or_404(Project, pk=kwargs.get('proekt_pk'))
        user = get_object_or_404(User, pk=kwargs.get('user_pk'))
        context = {
            'proekt': proekt,
            'user': user
        }
        return render(request, 'projects/delete_user.html', context)

    def post(self, request, *args, **kwargs):
        proekt = get_object_or_404(Project, pk=kwargs.get('proekt_pk'))
        user = get_object_or_404(User, pk=kwargs.get('user_pk'))
        proekt.users.remove(user)
        return redirect('webapp:project_view', pk=proekt.pk)

    def has_permission(self, **kwargs):
        return self.request.user.has_perm("webapp.remove_users_from_the_project")
