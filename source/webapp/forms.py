from django import forms
from django.forms import widgets
from webapp.models import Status, Type, TrackerIssue


# class TrackerIssueForm(forms.Form):
#     summary = forms.CharField(max_length=200, label='Заголовок', required=True)
#     description = forms.CharField(max_length=3000, label='Описание', required=False,
#                            widget=widgets.Textarea)
#     status = forms.ModelChoiceField(queryset=Status.objects.all(), required=False, label='Статус',
#                                       empty_label=None)
#     type = forms.ModelChoiceField(queryset=Type.objects.all(), required=False, label='Тип задачи',
#                                       empty_label=None)
#
#
# class StatusForm(forms.Form):
#     name = forms.CharField(max_length=20, label='Статус', required=False)
#
#
# class TypeForm(forms.Form):
#     name = forms.CharField(max_length=20, label='Тип', required=False)



class TrackerIssueForm(forms.ModelForm):
    class Meta:
        model = TrackerIssue
        fields =['summary', 'description', 'status', 'type']


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']