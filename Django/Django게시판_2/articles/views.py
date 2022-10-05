from django.shortcuts import redirect, render
from .models import Article
from .forms import ArticleForm
# Create your views here.

def index(request):
    articles = Article.objects.order_by('-pk')

    context = {
        'articles': articles
    }
    return render(request,'articles/index.html', context)

# def new(request):
#     return render(request, 'articles/new.html')

# def new(request):
#     article_form = ArticleForm()
#     context = {
#         'article_form': article_form
#     }
#     return render(request, 'articles/new.html',context=context)

def create(request):
    # title = request.GET.get('title')
    # content = request.GET.get('content')
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    
    # Article.objects.create(title=title, content=content)
    if request.method == 'POST':
        # DB에 저장하는 로직
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else: 
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/new.html', context=context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)

    # article_form = ArticleForm(instance=article)
    
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            
            return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm(instance=article)

    context = {
        'article_form': article_form
    }
    return render(request, 'articles/update.html', context)