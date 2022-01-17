from django import forms
from board.models import Article, Board, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article  # 사용할 모델
        board = Board
        fields = ['board', 'subject', 'content' ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # 사용할 모델
        fields = [ 'content' ]
