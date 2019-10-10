from django import forms
from webapp.models import Status, Type, TrackerIssue, Project


class TrackerIssueForm(forms.ModelForm):
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