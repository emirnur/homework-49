from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404


class DetailView(TemplateView):
    context_key = 'objects'
    model = None

    def get_context_data(self,pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_key] = self.get_objects(pk)
        return context

    def get_objects(self, pk):
        return get_object_or_404(self.model, pk=pk)

