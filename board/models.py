from django.db import models

# Create your models here.
class Board(models.Model):
    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    name = models.CharField('상품명(내부용)', max_length=100)
