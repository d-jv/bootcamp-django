# Generated by Django 3.2.5 on 2021-08-10 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_book_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.CharField(default='', max_length=255),
        ),
    ]