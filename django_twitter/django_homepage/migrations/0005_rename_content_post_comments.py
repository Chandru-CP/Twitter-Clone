# Generated by Django 4.2.4 on 2023-10-07 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_homepage', '0004_remove_comment_post_post_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='comments',
        ),
    ]
