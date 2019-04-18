# Generated by Django 2.2 on 2019-04-17 19:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_namegroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='tracker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.TrackerGroup'),
        ),
        migrations.RemoveField(
            model_name='namegroup',
            name='users',
        ),
        migrations.AddField(
            model_name='namegroup',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='response',
            name='answer',
        ),
        migrations.AddField(
            model_name='response',
            name='answer',
            field=models.ManyToManyField(to='core.Answer'),
        ),
        migrations.RemoveField(
            model_name='trackergroup',
            name='available_to',
        ),
        migrations.AddField(
            model_name='trackergroup',
            name='available_to',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]