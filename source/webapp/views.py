from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import TrackerIssue, Status, Type
from django.views import View
from django.views.generic import TemplateView
from webapp.forms import TrackerIssueForm, StatusForm, TypeForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = TrackerIssue.objects.all()
        return context


class IssueView(TemplateView):
    template_name = 'issue.html'

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(TrackerIssue, pk=pk)
        return context


class IssueCreateView(View):
    def get(self, request, *args, **kwargs):
        form = TrackerIssueForm()
        return render(request, 'issue_create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TrackerIssueForm(data=request.POST)
        if form.is_valid():
            issue = TrackerIssue.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                type=form.cleaned_data['type']
            )
            return redirect('issue_view', pk=issue.pk)
        else:
            return render(request, 'issue_create.html', context={'form': form})


class IssueUpdateView(View):

    def get(self, request, pk):
        issue = get_object_or_404(TrackerIssue, pk=pk)
        form = TrackerIssueForm(data={
            'summary': issue.summary,
            'description': issue.description,
            'status': issue.status_id,
            'type': issue.type_id
        })
        return render(request, 'issue_update.html', context={'form': form, 'issue': issue})

    def post(self, request, pk):
        issue = get_object_or_404(TrackerIssue, pk=pk)
        form = TrackerIssueForm(data=request.POST)
        if form.is_valid():
            issue.summary = form.cleaned_data['summary']
            issue.description = form.cleaned_data['description']
            issue.status = form.cleaned_data['status']
            issue.type = form.cleaned_data['type']
            issue.save()
            return redirect('issue_view', pk=issue.pk)
        else:
            return render(request, 'issue_update.html', context={'form': form, 'issue': issue})


class IssueDeleteView(View):

    def get(self, request, pk):
        issue = get_object_or_404(TrackerIssue, pk=pk)
        return render(request, 'issue_delete.html', context={'issue': issue})

    def post(self, request, pk):
        issue = get_object_or_404(TrackerIssue, pk=pk)
        issue.delete()
        return redirect('index')


class StatusView(TemplateView):
    template_name = 'status_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        return context


class StatusCreateView(View):
    def get(self, request, *args, **kwargs):
        form = StatusForm()
        return render(request, 'status_create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = StatusForm(data=request.POST)
        if form.is_valid():
            Status.objects.create(
                name=form.cleaned_data['name'],
            )
            return redirect('status_view')
        else:
            return render(request, 'status_create.html', context={'form': form})


class StatusUpdateView(View):

    def get(self, request, pk):
        status = get_object_or_404(Status, pk=pk)
        form = StatusForm(data={
            'name': status.name
        })
        return render(request, 'status_update.html', context={'form': form, 'status': status})

    def post(self, request, pk):
        status = get_object_or_404(Status, pk=pk)
        form = StatusForm(data=request.POST)
        if form.is_valid():
            status.name = form.cleaned_data['name']
            status.save()
            return redirect('status_view')
        else:
            return render(request, 'status_update.html', context={'form': form, 'status': status})


class StatusDeleteView(View):

    def get(self, request, pk):
        status = get_object_or_404(Status, pk=pk)
        return render(request, 'status_delete.html', context={'status': status})

    def post(self, request, pk):
        status = get_object_or_404(Status, pk=pk)
        status.delete()
        return redirect('status_view')


class TypeView(TemplateView):
    template_name = 'type_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['types'] = Type.objects.all()
        return context


class TypeCreateView(View):
    def get(self, request, *args, **kwargs):
        form = TypeForm()
        return render(request, 'type_create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TypeForm(data=request.POST)
        if form.is_valid():
            Type.objects.create(
                name=form.cleaned_data['name'],
            )
            return redirect('type_view')
        else:
            return render(request, 'type_create.html', context={'form': form})


class TypeUpdateView(View):

    def get(self, request, pk):
        typeof = get_object_or_404(Type, pk=pk)
        form = TypeForm(data={
            'name': typeof.name
        })
        return render(request, 'type_update.html', context={'form': form, 'type': typeof})

    def post(self, request, pk):
        typeof = get_object_or_404(Type, pk=pk)
        form = TypeForm(data=request.POST)
        if form.is_valid():
            typeof.name = form.cleaned_data['name']
            typeof.save()
            return redirect('type_view')
        else:
            return render(request, 'type_update.html', context={'form': form, 'type': typeof})


class TypeDeleteView(View):

    def get(self, request, pk):
        typeof = get_object_or_404(Type, pk=pk)
        return render(request, 'type_delete.html', context={'type': typeof})

    def post(self, request, pk):
        typeof = get_object_or_404(Type, pk=pk)
        typeof.delete()
        return redirect('type_view')

