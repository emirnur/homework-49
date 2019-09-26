from django import forms
from django.forms import widgets
from webapp.models import Status, Type


class TrackerIssueForm(forms.Form):
    summary = forms.CharField(max_length=200, label='Заголовок', required=True)
    description = forms.CharField(max_length=3000, label='Описание', required=False,
                           widget=widgets.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=False, label='Статус',
                                      empty_label=None)
    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=False, label='Тип задачи',
                                      empty_label=None)