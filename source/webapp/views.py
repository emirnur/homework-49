from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import TrackerIssue
from django.views import View
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = TrackerIssue.objects.all()
        return context


class IssueView(TemplateView):
    template_name = 'issue.html'

    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(TrackerIssue, pk=pk)
        return context

#
# class ArticleCreateView(View):
#     def get(self, request, *args, **kwargs):
#         form = ArticleForm()
#         return render(request, 'create.html', context={'form': form})
#
#     def post(self, request, *args, **kwargs):
#         form = ArticleForm(data=request.POST)
#         if form.is_valid():
#             article = Article.objects.create(
#                 title=form.cleaned_data['title'],
#                 author=form.cleaned_data['author'],
#                 text=form.cleaned_data['text'],
#                 category=form.cleaned_data['category']
#             )
#             return redirect('article_view', pk=article.pk)
#         else:
#             return render(request, 'create.html', context={'form': form})
#
#
# def article_update_view(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     if request.method == 'GET':
#         form = ArticleForm(data={
#             'title': article.title,
#             'author': article.author,
#             'text': article.text,
#             'category': article.category_id
#         })
#         return render(request, 'update.html', context={'form': form, 'article': article})
#     elif request.method == 'POST':
#         form = ArticleForm(data=request.POST)
#         if form.is_valid():
#             article.title = form.cleaned_data['title']
#             article.author = form.cleaned_data['author']
#             article.text = form.cleaned_data['text']
#             article.category = form.cleaned_data['category']
#             article.save()
#             return redirect('article_view', pk=article.pk)
#         else:
#             return render(request, 'update.html', context={'form': form, 'article': article})
#
#
# def article_delete_view(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     if request.method == 'GET':
#         return render(request, 'delete.html', context={'article': article})
#     elif request.method == 'POST':
#         article.delete()
#         return redirect('index')