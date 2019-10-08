from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.models import Status
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView
from webapp.forms import StatusForm
from webapp.views.base_views import UpdateView


class StatusView(ListView):
    template_name = 'status/status_index.html'
    context_object_name = 'statuses'
    model = Status


class StatusCreateView(CreateView):
    template_name = 'status/status_create.html'
    model = Status

    fields = ['name']

    def get_success_url(self):
        return reverse('status_view')


class StatusUpdateView(UpdateView):
    model = Status
    template_name = 'status/status_update.html'
    form_class = StatusForm
    context_object_name = 'status'

    def get_redirect_url(self):
        return reverse('status_view')


class StatusDeleteView(View):

    def get(self, request, pk):
        status = get_object_or_404(Status, pk=pk)
        return render(request, 'status/status_delete.html', context={'status': status})

    def post(self, request, pk):
        status = get_object_or_404(Status, pk=pk)
        status.delete()
        return redirect('status_view')

