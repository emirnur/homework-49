from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

from webapp.models import Status
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from webapp.forms import StatusForm


class StatusView(ListView):
    template_name = 'status/status_index.html'
    context_object_name = 'statuses'
    model = Status


class StatusCreateView(CreateView):
    template_name = 'status/status_create.html'
    model = Status

    fields = ['name']

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('status_view')


class StatusUpdateView(UpdateView):
    model = Status
    template_name = 'status/status_update.html'
    form_class = StatusForm
    context_object_name = 'status'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('status_view')


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'status/status_delete.html'
    model = Status
    context_object_name = 'status'
    success_url = reverse_lazy('status_view')

