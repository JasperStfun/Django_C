from django.shortcuts import render, redirect
from django.views.generic import DetailView

from .models import Article
from .forms import ArticleForm


def news_home(request):
    news = Article.objects.order_by('-pub_date')[:3]
    data = {
        'title': 'Главные новости'
    }
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Article
    template_name = 'news/detail_views.html'
    context_object_name = 'article'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('./')
        else:
            error = 'Форма неверно заполнена.'

    form = ArticleForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)
