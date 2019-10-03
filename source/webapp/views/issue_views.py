from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import TrackerIssue
from django.views import View
from django.views.generic import TemplateView, ListView
from webapp.forms import TrackerIssueForm


class IndexView(ListView):
    template_name = 'issue/index.html'
    context_object_name = 'issues'
    model = TrackerIssue
    ordering = ['-created_at']
    paginate_by = 3
    paginate_orphans = 1


class IssueView(TemplateView):
    template_name = 'issue/issue.html'

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(TrackerIssue, pk=pk)
        return context


class IssueCreateView(View):
    def get(self, request, *args, **kwargs):
        form = TrackerIssueForm()
        return render(request, 'issue/issue_create.html', context={'form': form})

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
            return render(request, 'issue/issue_create.html', context={'form': form})


class IssueUpdateView(View):

    def get(self, request, pk):
        issue = get_object_or_404(TrackerIssue, pk=pk)
        form = TrackerIssueForm(data={
            'summary': issue.summary,
            'description': issue.description,
            'status': issue.status_id,
            'type': issue.type_id
        })
        return render(request, 'issue/issue_update.html', context={'form': form, 'issue': issue})

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
            return render(request, 'issue/issue_update.html', context={'form': form, 'issue': issue})


class IssueDeleteView(View):

    def get(self, request, pk):
        issue = get_object_or_404(TrackerIssue, pk=pk)
        return render(request, 'issue/issue_delete.html', context={'issue': issue})

    def post(self, request, pk):
        issue = get_object_or_404(TrackerIssue, pk=pk)
        issue.delete()
        return redirect('index')