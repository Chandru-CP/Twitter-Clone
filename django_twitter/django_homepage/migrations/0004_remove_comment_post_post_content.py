# Generated by Django 4.2.4 on 2023-10-07 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_homepage', '0003_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.ManyToManyField(to='django_homepage.comment'),
        ),
    ]