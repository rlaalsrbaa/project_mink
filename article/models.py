from django.db import models
from accounts.models import User
# Create your models here.

class Article(models.Model):
    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('수정날짜', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField('제목', max_length=100)
    content = models.TextField('내용')
    is_blind = models.BooleanField('공개 여부', default=False)
