from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Article, Comment, Hashtag
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

            # Hash tag 저장 로직 (article이 저장되야 pk값 사용가능)
            for word in article.content.split(): # 공백을 기준으로 리스트
                if word[0] == '#':
                    # word랑 같은 해시태그 존재하면, 기존 객체 반환, 없으면 새로운 객체 생성
                    hashtag, created = Hashtag.objects.get_or_create(content=word)
                    # 1. 현재 등록된 모든 해시태그 보기
                    # 2. 클릭시 Hash 태그 기준으로 filter 해주기
                    # 3. 게시물 수정 시, 새로 등록된 해시태그 검사 해주기

                    article.hashtags.add(hashtag)

            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()

    context = {'form': form}
    return render(request, 'articles/create.html', context)

# 2. 클릭시 Hash 태그 기준으로 filter 해주기
# 특정 해시태그를 포함한 글 리스트 보여주기
def hashtag_filtering(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)
    articles = hashtag.article_set.order_by('-pk')

    context = {
        'hashtag': hashtag,
        'articles': articles,
    }

    return render(request, 'articles/hashtag.html', context)


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