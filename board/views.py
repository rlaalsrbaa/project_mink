# Create your views here.
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .forms import ArticleForm
from board.models import Board, Article


def notice(request: HttpRequest):
    board = Board.objects.get(name="공지사항")

    return article_list(request, board)

def article_list(request: HttpRequest, board):
    kw = request.GET.get('kw', '')
    page = request.GET.get('page', '1')  # 페이지

    if not kw:
        article_list = Article.objects.filter(board=board.id).order_by('-id')
    else:
        article_list = Article.objects.filter(board=board.id,subject__icontains=kw).order_by('-id')

    paginator = Paginator(article_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'article_list': page_obj,
               'board': board,
               }
    return render(request, 'board/article_list.html', context)

def article_detail(request: HttpRequest, article_id):
    return render(request, 'board/article_detail.html',)


def article_write(request: HttpRequest, board_id):
    board = Board.objects.get(id=board_id)
    returnUrl = f"board/{board.id}"
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.board_id = board.id
            article.user_id = request.user.id
            article.save()
            return redirect(returnUrl)
    else:
        form = ArticleForm()
    context = {'form': form,
               'board': board}
    return render(request, 'board/article_form.html', context)