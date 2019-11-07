from django import forms
from webapp.models import Status, Type, TrackerIssue, Project


class TrackerIssueForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # print(kwargs)
        self.user = kwargs.pop('created_by')
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        issue = super().save(commit=False)
        issue.created_by = self.user
        if commit:
            issue.save()
        return issue


    class Meta:
        model = TrackerIssue
        fields = ['summary', 'description', 'status', 'type', 'project']


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")