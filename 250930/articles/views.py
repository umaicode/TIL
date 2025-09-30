from django.shortcuts import render, redirect

# Create your views here.

from .models import Article


def index(request):
    # QuerySet API -> 전체데이터조회
    articles = Article.objects.all()

    context = {
        "articles": articles,
    }

    # 단순 조회목적, GET방식이면 render
    # 생성, 수정, 삭제 POST방식이면 redirect
    return render(request, "articles/index.html", context)


# 단일 게시글 페이지를 렌더링
def detail(request, pk):
    # QuerySet API -> 단일게시글조회 : get
    article = Article.objects.get(pk=pk)
    context = {"article": article}
    return render(request, "articles/detail.html", context)


from .forms import ArticleForm


def create(request):
    # 내가(클라이언트) 게시글 생성 버튼을 눌렀을 때
    # 폼을 다 작성하고, 게시글 생성 버튼을 눌렀을 때
    if request.method == "POST":
        form = ArticleForm(request.POST)
        # 유효성 검사
        # 1. 모든 필수 필드가 다 채워져 있는지
        # 2. 입력된 데이터가 필드의 조건 ( ex) 데이터 형식, 길이 제한)을 만족하는지
        if form.is_valid():
            article = form.save()
            # DB 건드린다 -> redirect
            return redirect("articles:detail", article.pk)

    # POST 방식을 제외한 모든 경우
    # 게시글 생성 버튼을 누르기 전 또는 다른 버튼을 눌렀을 때
    else:
        form = ArticleForm()  # 아무것도 없는 빈 폼

    # GET 요청인 경우 -> 홈페이지에서 create버튼 눌렀을 때
    context = {
        "form": form,
    }

    return render(request, "articles/create.html", context)


# # GET방식(단순히 페이지를 랜더링)
# def new(request):
#     return render(request, "articles/new.html")


# # POST방식(게시글 생성 - DB 저장)
# def create(request):
#     # form태그의 name -> title, content
#     # GET방식은 단순 조회목적
#     # ex) 데이터를 단순 조회하거나 검색
#     # POST방식은 DB를 건든다.(보안과 관련)
#     # ex) 데이터를 생성, 수정, 삭제
#     title = request.POST.get("title")
#     content = request.POST.get("content")

#     # ORM의 2번 방법(코드가 간결하면서도 안정성)
#     # 안정성 : 데이터 관리(저장) 원칙
#     # save()하기전에 유효성 검사!!!
#     article = Article(title=title, content=content)
#     article.save()

#     # app_name = articles
#     # name = detail
#     return redirect("articles:detail", article.pk)


def delete(request, pk):
    # 먼저 조회
    article = Article.objects.get(pk=pk)
    # 조회 후 삭제
    article.delete()
    # render? redirect?
    # DB를 건든다. POST방식이다. redirect
    return redirect("articles:index")


# update와 create의 차이 : 기존에 있던 게시글을 조회
# GET 방식
# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     context = {
#         "article": article,
#     }

#     return render(request, "articles/edit.html", context)


# POST 방식
# def update(request, pk):
#     # 조회 후
#     article = Article.objects.get(pk=pk)
#     # 수정
#     article.title = request.POST.get("title")
#     article.content = request.POST.get("content")

#     # 저장
#     article.save()
#     return redirect("articles:detail", article.pk)


def update(request, pk):
    # create와 edit의 차이 : update는 조회 먼저 하고 수정
    article = Article.objects.get(pk=pk)
    # 게시글 수정 버튼 눌렀을 때
    if request.method == "POST":
        # instance = article : 기존 게시글의 데이터를 가져온다.
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("articles:detail", article.pk)

    # 게시글 수정 버튼 누르기 전 또는 다른 버튼 눌렀을 때
    else:
        form = ArticleForm(instance=article)

    # GET 요청
    context = {
        "article": article,
        "form": form,  # 기존에 있던 데이터
    }

    return render(request, "articles/update.html", context)
