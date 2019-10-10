from django.urls import reverse, reverse_lazy
from webapp.models import Type
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from webapp.forms import TypeForm


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

    def get_success_url(self):
        return reverse('type_view')


class TypeDeleteView(DeleteView):
    template_name = 'type/type_delete.html'
    model = Type
    context_object_name = 'type'
    success_url = reverse_lazy('type_view')

