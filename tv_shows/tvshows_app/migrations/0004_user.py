# Generated by Django 3.2.5 on 2021-08-28 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows_app', '0003_alter_network_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('alllowed', models.BooleanField(default=True)),
                ('avatar', models.URLField(default='https://icon-library.com/images/coder-icon/coder-icon-26.jpg')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
