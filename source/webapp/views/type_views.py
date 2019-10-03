from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Type
from django.views import View
from django.views.generic import TemplateView, ListView
from webapp.forms import TypeForm


class TypeView(ListView):
    template_name = 'type/type_index.html'
    context_object_name = 'types'
    model = Type


class TypeCreateView(View):
    def get(self, request, *args, **kwargs):
        form = TypeForm()
        return render(request, 'type/type_create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TypeForm(data=request.POST)
        if form.is_valid():
            Type.objects.create(
                name=form.cleaned_data['name'],
            )
            return redirect('type_view')
        else:
            return render(request, 'type/type_create.html', context={'form': form})


class TypeUpdateView(View):

    def get(self, request, pk):
        typeof = get_object_or_404(Type, pk=pk)
        form = TypeForm(data={
            'name': typeof.name
        })
        return render(request, 'type/type_update.html', context={'form': form, 'type': typeof})

    def post(self, request, pk):
        typeof = get_object_or_404(Type, pk=pk)
        form = TypeForm(data=request.POST)
        if form.is_valid():
            typeof.name = form.cleaned_data['name']
            typeof.save()
            return redirect('type_view')
        else:
            return render(request, 'type/type_update.html', context={'form': form, 'type': typeof})


class TypeDeleteView(View):

    def get(self, request, pk):
        typeof = get_object_or_404(Type, pk=pk)
        return render(request, 'type/type_delete.html', context={'type': typeof})

    def post(self, request, pk):
        typeof = get_object_or_404(Type, pk=pk)
        typeof.delete()
        return redirect('type_view')

