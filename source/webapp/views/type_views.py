from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.models import Type
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView
from webapp.forms import TypeForm
from webapp.views.base_views import UpdateView


class TypeView(ListView):
    template_name = 'type/type_index.html'
    context_object_name = 'types'
    model = Type


class TypeCreateView(CreateView):
    template_name = 'type/type_create.html'
    model = Type

    fields = ['name']

    def get_success_url(self):
        return reverse('type_view')


class TypeUpdateView(UpdateView):
    model = Type
    template_name = 'type/type_update.html'
    form_class = TypeForm
    context_object_name = 'type'

    def get_redirect_url(self):
        return reverse('type_view')


class TypeDeleteView(View):

    def get(self, request, pk):
        typeof = get_object_or_404(Type, pk=pk)
        return render(request, 'type/type_delete.html', context={'type': typeof})

    def post(self, request, pk):
        typeof = get_object_or_404(Type, pk=pk)
        typeof.delete()
        return redirect('type_view')

