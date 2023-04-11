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
    # Comment 작성폼
    commentForm = CommentForm() # 빈 폼
    # 이미 작성된 Comment List
    # comment_list = article.comment_set.all()

    # SELECT * FROM Comment WHERE parent IS NULL;
    comment_list = article.comment_set.filter(parent__isnull=True) # 댓글
    context = {
        'article': article,
        'commentForm': commentForm,
        'comment_list': comment_list,
    }

    return render(request, 'articles/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()

    context = {'form': form}
    return render(request, 'articles/create.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)

    context = {'form': form, 'article': article}
    return render(request, 'articles/update.html', context)


#############################################################################


def create_comment(request, pk):
    # 작성할 article 객체 불러오기
    article = Article.objects.get(pk=pk)

    # modelForm
    commentForm = CommentForm(request.POST) # 사용자 입력값 받아와서, 폼 인스턴스까지

    parent_pk = request.POST.get('parent_pk')

    # 댓글이던 답글이던 일단 validation은 통과해야겠다
    if commentForm.is_valid():
        # article에 의존성이 있는데 아직 article을 넣어주지 않음
        comment = commentForm.save(commit=False) # TCL
        comment.article = article # 의존성을 장고에서 줄때는 instance 자체를 참조값으로 줘야함
        
        # 얘가 댓글인지 답글인지 넣어주자
        if parent_pk:
            parent_comment = Comment.objects.get(pk=parent_pk)
            comment.parent = parent_comment
        comment.save()

    return redirect('articles:detail', article.pk)