# Create your views here.
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from board.models import Board, Article


def notice(request: HttpRequest):
    board = Board.objects.get(name="공지사항")
    return article_list(request, board)

def article_list(request: HttpRequest, board):
    page = request.GET.get('page', '1')  # 페이지

    # 조회
    article_list = Article.objects.filter(board_id=board.id).order_by('-id')

    # 페이징처리
    paginator = Paginator(article_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'article_list': page_obj}
    return render(request, 'board/list.html', context)

def article_detail(request: HttpRequest, article_id):
    return HttpResponse("응답")