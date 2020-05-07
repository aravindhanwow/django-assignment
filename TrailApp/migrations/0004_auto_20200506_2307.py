# Generated by Django 3.0.5 on 2020-05-06 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrailApp', '0003_auto_20200506_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity_period',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='activity_period',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='activity_period',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='activity_period',
            name='start_time',
        ),
        migrations.AlterField(
            model_name='activity_period',
            name='end_datetime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='activity_period',
            name='start_datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]