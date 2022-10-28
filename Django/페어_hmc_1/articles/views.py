from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required

from .forms import ArticleForm, MakeCommentForm

from .models import Article
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_safe
from django.core.paginator import Paginator




@require_safe

def index(request):
    page = request.GET.get('page','1')
    articles = Article.objects.order_by('-pk')
    paginator = Paginator(articles,10)
    page_obj = paginator.get_page(page)
    context = {
        'articles': page_obj
    }

    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        articleform = ArticleForm(request.POST, request.FILES)
        if articleform.is_valid():
            article = articleform.save(commit=False)
            article.user = request.user
            article.save()
            print(4)
            return redirect('articles:index')
    else:
        articleform = ArticleForm()
    context = {
        'article_form': articleform
    }
    return render(request, 'articles/create.html', context)

@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            articleform = ArticleForm(request.POST, request.FILES, instance=article)
            if articleform.is_valid():
                articleform.save()
                return redirect('articles:detail', article.pk)
        else:
            articleform = ArticleForm(instance=article)
        context = {
            'articleform': articleform
        }
        return render(request, 'articles/update.html', context)
    else:
        return redirect('articles:detail', article.pk)

@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        article.delete()
        return redirect('articles:index')


def detail(request,pk):
    articles = Article.objects.get(pk=pk)
    commentform = MakeCommentForm()
    context={
        'articles':articles,
        'commentform':commentform,
    }
    return render(request,"articles/detail.html",context)


def comment(request, pk):

    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        form = MakeCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.article = article
            comment.save()
            return render (request,"articles/detail.html",pk)

