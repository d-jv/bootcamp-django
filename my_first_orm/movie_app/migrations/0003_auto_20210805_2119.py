# Generated by Django 3.2.5 on 2021-08-06 01:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_users_wizard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wizard',
            name='year',
        ),
        migrations.AddField(
            model_name='wizard',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wizard',
            name='position',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wizard',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
