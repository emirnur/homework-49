from urllib import request
from urllib.parse import urlencode

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from webapp.models import TrackerIssue, Project, Team
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from webapp.forms import TrackerIssueForm, SimpleSearchForm
from webapp.views.base_views import DetailView


class UserProjectIssue:
    def checker(self, project, user):
        if project:
            project = Project.objects.get(pk=project)
            for user_obj in project.team_project.all():
                return user_obj.user == user


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


class IssueCreateView(PermissionRequiredMixin, UserProjectIssue, CreateView):
    template_name = 'issue/issue_create.html'
    model = TrackerIssue
    form_class = TrackerIssueForm
    permission_required = 'webapp.webapp.add_trackerissue'
    permission_denied_message = 'You have no permissions!'

    # fields = ['summary', 'description', 'status', 'type', 'project', 'created_by', 'assigned_to']

    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        form.fields.pop('created_by')
        form.fields.pop('project')
        return form


    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs['project'] = get_object_or_404(Project, pk=self.kwargs['pk'])
    #     return kwargs

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['project'] = get_object_or_404(Project, pk=self.kwargs['pk'])
        return kwargs

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     context['project'] = get_object_or_404(Project, pk=self.kwargs['pk'])

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:issue_view', kwargs={'pk': self.object.pk})

    # def form_valid(self, form):
    #     project = self.request.POST.get('project')
    #     if self.checker(project, self.request.user) is True:
    #         return super().form_valid(form)
    #     else:
    #         return render(self.request, 'issue/invalid.html')


class IssueUpdateView(PermissionRequiredMixin, UserProjectIssue, UpdateView):
    model = TrackerIssue
    template_name = 'issue/issue_update.html'
    form_class = TrackerIssueForm
    context_object_name = 'issue'
    permission_required = 'webapp.change_trackerissue'
    permission_denied_message = 'You have no permissions!'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:issue_view', kwargs={'pk': self.object.pk})

    # def form_valid(self, form):
    #     project = self.request.POST.get('project')
    #     if self.checker(project, self.request.user) is True:
    #         return super().form_valid(form)
    #     else:
    #         return render(self.request, 'issue/invalid.html')

    # def get(self, request, *args, **kwargs):
    #     issue = TrackerIssue.objects.get(pk=kwargs.get('pk'))
    #     project = issue.project.pk
    #
    #     if self.checker(project, self.request.user):
    #         return super().get(request, *args, **kwargs)
    #     else:
    #         return render(self.request, 'issue/invalid.html')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        form.fields.pop('created_by')
        form.fields.pop('project')
        return form

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        print(self.kwargs['pk'])
        issue = get_object_or_404(TrackerIssue, pk=self.kwargs['pk'])
        kwargs['project'] = Project.objects.get(issues_project=issue)
        return kwargs


class IssueDeleteView(UserProjectIssue, LoginRequiredMixin, PermissionRequiredMixin,  DeleteView):
    template_name = 'issue/issue_delete.html'
    model = TrackerIssue
    context_object_name = 'issue'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_trackerissue'
    permission_denied_message = 'You have no permissions!'

    def get(self, request, *args, **kwargs):
        issue = TrackerIssue.objects.get(pk=kwargs.get('pk'))
        project = issue.project.pk

        if self.checker(project, self.request.user):
            return super().get(request, *args, **kwargs)
        else:
            return render(self.request, 'issue/invalid.html')






