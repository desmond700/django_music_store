# Generated by Django 2.1.2 on 2018-10-26 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20181022_1104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='body',
        ),
        migrations.RemoveField(
            model_name='music',
            name='title',
        ),
        migrations.AddField(
            model_name='music',
            name='artist',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='music',
            name='genre',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='music',
            name='song_title',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='music',
            name='song_url',
            field=models.TextField(default=None),
        ),
    ]
