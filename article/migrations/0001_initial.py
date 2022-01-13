# Generated by Django 4.0.1 on 2022-01-13 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='수정날짜')),
                ('subject', models.CharField(max_length=100, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('is_blind', models.BooleanField(default=False, verbose_name='공개 여부')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
