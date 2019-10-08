from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.models import TrackerIssue
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from webapp.forms import TrackerIssueForm
from webapp.views.base_views import DetailView, UpdateView, DeleteView


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

    fields = ['summary', 'description', 'status', 'type']

    def get_success_url(self):
        return reverse('issue_view', kwargs={'pk': self.object.pk})


class IssueUpdateView(UpdateView):
    model = TrackerIssue
    template_name = 'issue/issue_update.html'
    form_class = TrackerIssueForm
    context_object_name = 'issue'

    def get_redirect_url(self):
        return reverse('issue_view', kwargs={'pk': self.object.pk})


class IssueDeleteView(DeleteView):
    template_name = 'issue/issue_delete.html'
    model = TrackerIssue
    context_object_name = 'issue'
    confirm_deletion = True

    def get_redirect_url(self):
        return reverse('index')