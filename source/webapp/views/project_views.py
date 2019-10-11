from django.urls import reverse, reverse_lazy

from webapp.forms import ProjectForm
from webapp.models import Project
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ProjectIndex(ListView):
    template_name = 'project/project_index.html'
    context_object_name = 'projects'
    model = Project
    ordering = ['created_at']
    paginate_by = 3
    paginate_orphans = 1


class ProjectView(DetailView):
    template_name = 'project/project.html'
    context_key = 'project'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        issues = project.issues.order_by('-created_at')
        context['issues'] = issues
        return context


class ProjectCreateView(CreateView):
    template_name = 'project/project_create.html'
    model = Project

    fields = ['title', 'description']

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'project/project_update.html'
    form_class = ProjectForm
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(DeleteView):
    template_name = 'project/project_delete.html'
    model = Project
    context_object_name = 'project'
    success_url = reverse_lazy('project_index')