# Generated by Django 4.2.4 on 2023-09-10 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]