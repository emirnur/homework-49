from django import forms
from django.contrib.auth.models import User

from webapp.models import Status, Type, TrackerIssue, Project


class TrackerIssueForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        print('here')
        print(kwargs, 'here')
        self.user = kwargs.pop('user')
        self.project = kwargs.pop('project')
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'] = forms.ModelChoiceField(queryset=User.objects.filter(team_user__project=self.project), required=False)

    def save(self, commit=True):
        issue = super().save(commit=False)
        issue.created_by = self.user
        issue.project = self.project
        if commit:
            issue.save()
        return issue


    class Meta:
        model = TrackerIssue
        fields = ['summary', 'description', 'status', 'type', 'project', 'created_by', 'assigned_to']


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