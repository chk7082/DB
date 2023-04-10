from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()

    comments = article.comment_set.all() # 역참조 필요

    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()

    context = {'form': form}
    return render(request, 'articles/create.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)
    

def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', pk=article.pk)
        else:
            form = ArticleForm(instance=article)
        context = {'form': form, 'article': article}
        return render(request, 'articles/update.html', context)
    
    else:
        return redirect('articles:index')


def comments_create(request, pk):
    # comment 저장 로직을 돌려줘야할듯
    article = Article.objects.get(pk=pk)

    # 저 안에 아무것도 안채우면, 빈 폼
    # 저 안에 POST로 받은걸 채우면, 사용자 입력을 채워준다
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        # 바로 세이브하는게 아니라, 세이브 하기전에 comment instance에 접근해서
        # save 하기 전에 실제로 데이터 베이스에 반영하기 전에 나한테 잠시만 줄래?
        # article 어디인지 달아줘야함

        # 저장하기 전에 잠시 기다리고, 만든거를 comment라는 instance에 담아줘
        comment = comment_form.save(commit=False)
        comment.article = article          # 해야했던거 진행하자
        comment.save()
    return redirect('articles:detail', article.pk)


def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
