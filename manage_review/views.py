from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article
# Create your views here.

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts')  
    else:
        form = ArticleForm()

    return render(request, 'create_article.html', {'form': form})

def posts(request):
    articles = Article.objects.all()
    return render(request, 'posts.html', {'articles': articles})