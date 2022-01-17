# Create your views here.
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
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
        article_list = Article.objects.filter(board=board.id,).filter(Q (subject__icontains=kw) | Q (content__icontains=kw)).order_by('-id')

    paginator = Paginator(article_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'article_list': page_obj,
               'board': board,
               }
    return render(request, 'board/article_list.html', context)

def article_detail(request: HttpRequest, article_id):
    article = get_object_or_404(Article, id=article_id)
    board = get_object_or_404(Board, id=article.board_id)
    context = {'article': article,
               'board': board}
    return render(request, 'board/article_detail.html', context)


def article_write(request: HttpRequest, board_id):
    if request.user.is_authenticated:
        board = Board.objects.get(id=board_id)
        returnUrl = f"/board/{board.id}"
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
    else:
        return redirect('accounts:login')

def article_modify(request: HttpRequest, article_id):
    article = get_object_or_404(Article, id=article_id)
    board_id = article.board_id
    board = get_object_or_404(Board, id=board_id)
    if request.user.id == article.user_id:
        if request.method == "POST":
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                messages.success(request, "질문이 수정되었습니다.")
                return redirect(f"/board/{board_id}")
        else:
            form = ArticleForm(None, instance=article)

        return render(request, "board/article_form.html", {
            "form": form,
            "board": board,
        })
    else:
        return redirect('index')
def article_delete(request: HttpRequest, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.user.id == article.user_id:
        board_id = article.board_id
        article.delete()
        messages.success(request, "질문이 삭제되었습니다.")

        return redirect(f"/board/{board_id}")
    else:
        return redirect('index')