# Generated by Django 4.2.4 on 2023-10-07 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_homepage', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='django_homepage.post'),
            preserve_default=False,
        ),
    ]
