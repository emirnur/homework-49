from datetime import datetime
from urllib.parse import urlencode

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy

from webapp.forms import ProjectForm, SimpleSearchForm
from webapp.models import Project, Team
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ProjectIndex(ListView):
    template_name = 'project/project_index.html'
    context_object_name = 'projects'
    model = Project
    ordering = ['created_at']
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
                Q(title__icontains=self.search_value)
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


class ProjectView(DetailView):
    template_name = 'project/project.html'
    context_key = 'project'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        issues = project.issues_project.order_by('-created_at')
        context['issues'] = issues
        users = Team.objects.filter(project=self.object, date_end=None)
        context['users'] = users
        return context


class ProjectCreateView(CreateView):
    template_name = 'project/project_create.html'
    model = Project
    form_class = ProjectForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        users = form.cleaned_data.pop('users')
        self.object = form.save()
        list_users = list(users)
        Team.objects.create(user=self.request.user, date_start=datetime.now(), project=self.object)
        for user in list_users:
            Team.objects.create(user=user, project=self.object, date_start=datetime.now())

        return redirect(self.get_success_url())


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'project/project_update.html'
    form_class = ProjectForm
    context_object_name = 'project'

    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        form.fields.pop('users')
        return form

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'project/project_delete.html'
    model = Project
    context_object_name = 'project'
    success_url = reverse_lazy('webapp:project_index')


class TeamUserDelete(LoginRequiredMixin, DeleteView):
    model = Team

    def delete(self, request, *args, **kwargs):
        print(kwargs)
        self.object = self.get_object()
        print(self.object)
        self.object.date_end = datetime.now()
        self.object.save()
        return redirect(reverse('webapp:project_view', kwargs={'pk': self.object.project.pk}))
