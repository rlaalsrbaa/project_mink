# Generated by Django 4.0.1 on 2022-01-17 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_article'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='Board',
            new_name='board',
        ),
        migrations.AddField(
            model_name='article',
            name='votes',
            field=models.IntegerField(default=0, verbose_name='추천수'),
        ),
    ]