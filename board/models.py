from django.db import models
from accounts.models import User


# Create your models here.
class Board(models.Model):
    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    name = models.CharField('상품명(내부용)', max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('수정날짜', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    subject = models.CharField('제목', max_length=100)
    content = models.TextField('내용')
    votes = models.IntegerField("추천수", default=0, )
    is_blind = models.BooleanField('공개 여부', default=False)
    how_many_comment = models.IntegerField("댓글수", default=0)

    def __str__(self):
        return self.subject

class Comment(models.Model):
    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('수정날짜', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField('내용')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    is_modify = models.BooleanField('수정 가능 여부', default=False)
