from django.shortcuts import render

from .models import Article


def news_home(request):
    news = Article.objects.order_by('-pub_date')
    data = {
        'title': 'Главные новости'
    }
    return render(request, 'news/news_home.html', {'news': news})
