from urllib.parse import urlencode

from django.db.models import Q
from django.urls import reverse, reverse_lazy
from webapp.models import TrackerIssue
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from webapp.forms import TrackerIssueForm, SimpleSearchForm
from webapp.views.base_views import DetailView


class IndexView(ListView):
    template_name = 'issue/index.html'
    context_object_name = 'issues'
    model = TrackerIssue
    ordering = ['-created_at']
    paginate_by = 2
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(summary__icontains=self.search_value)
                | Q(description__icontains=self.search_value)
            )
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_search_form(self):
        return SimpleSearchForm(data=self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


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