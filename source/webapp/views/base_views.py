from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render, redirect


class DetailView(TemplateView):
    context_key = 'objects'
    model = None

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_key] = self.get_objects(pk)
        return context

    def get_objects(self, pk):
        return get_object_or_404(self.model, pk=pk)


class UpdateView(View):
    form_class = None
    template_name = None
    redirect_url = ''
    model = None
    pk_kwargs_url = 'pk'
    context_object_name = None
    object = None

    def get(self, request, *args, **kwargs):
        data = self.get_object()
        form = self.form_class(instance=data)
        return render(request, self.template_name, context={'form': form, self.context_object_name: data})

    def post(self, request, *args, **kwargs):
        data = self.get_object()
        form = self.form_class(instance=data, data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_redirect_url(self):
        return self.redirect_url

    def form_valid(self, form):
        self.object = self.get_object()
        form.save()
        return redirect(self.get_redirect_url())

    def form_invalid(self, form):
        return render(self.request, self.template_name, context={'form': form})

    def get_object(self):
        pk = self.kwargs.get(self.pk_kwargs_url)
        data = get_object_or_404(self.model, pk=pk)
        return data