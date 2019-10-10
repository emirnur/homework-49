from django.urls import reverse, reverse_lazy
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


# class IssueCreateView(CreateView):
#     template_name = 'issue/issue_create.html'
#     model = TrackerIssue
#
#     fields = ['summary', 'description', 'status', 'type']
#
#     def get_success_url(self):
#         return reverse('issue_view', kwargs={'pk': self.object.pk})
#
#
# class IssueUpdateView(UpdateView):
#     model = TrackerIssue
#     template_name = 'issue/issue_update.html'
#     form_class = TrackerIssueForm
#     context_object_name = 'issue'
#
#     def get_success_url(self):
#         return reverse('issue_view', kwargs={'pk': self.object.pk})
#
#
# class IssueDeleteView(DeleteView):
#     template_name = 'issue/issue_delete.html'
#     model = TrackerIssue
#     context_object_name = 'issue'
#     success_url = reverse_lazy('index')