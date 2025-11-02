from django.shortcuts import render, get_object_or_404
from .models import Article

def liste_articles(request):
    articles = Article.objects.all().order_by('-date_publication')
    return render(request, 'blog/liste_articles.html', {'articles': articles})

def detail_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'blog/detail_article.html', {'article': article})
