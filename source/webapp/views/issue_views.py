from django.urls import reverse, reverse_lazy
from webapp.models import TrackerIssue
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from webapp.forms import TrackerIssueForm
from webapp.views.base_views import DetailView


class IndexView(ListView):
    template_name = 'issue/index.html'
    context_object_name = 'issues'
    model = TrackerIssue
    ordering = ['-created_at']
    paginate_by = 3
    paginate_orphans = 1


class IssueView(DetailView):
    template_name = 'issue/issue.html'
    context_key = 'issue'
    model = TrackerIssue


class IssueCreateView(CreateView):
    template_name = 'issue/issue_create.html'
    model = TrackerIssue

    fields = ['summary', 'description', 'status', 'type', 'project']

    def get_success_url(self):
        return reverse('issue_view', kwargs={'pk': self.object.pk})


class IssueUpdateView(UpdateView):
    model = TrackerIssue
    template_name = 'issue/issue_update.html'
    form_class = TrackerIssueForm
    context_object_name = 'issue'

    def get_success_url(self):
        return reverse('issue_view', kwargs={'pk': self.object.pk})


class IssueDeleteView(DeleteView):
    template_name = 'issue/issue_delete.html'
    model = TrackerIssue
    context_object_name = 'issue'
    success_url = reverse_lazy('index')