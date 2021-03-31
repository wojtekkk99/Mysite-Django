from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from django.http import HttpResponse
from . import forms

# Create your views here.
def article_list(request):
    articles = Article.objects.all()

    # 1 żadanie, 2 przekierowanie, 3 przekazywanie słownika danych 
    return render(request, 'articles/article_list.html', {'articles': articles}) 

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})

@login_required(login_url='/accounts/login')
def create_article(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # pobieramy dane do zapisania i dajemy do zmienej i nie zapisujemy jeszcze
            # dopisujemy autora - user znajduje się w requescie
            to_save = form.save(commit=False)
            to_save.author = request.user
            to_save.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle
    return render(request, 'articles/article_create.html', {'form': form})