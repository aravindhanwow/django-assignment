# Generated by Django 3.0.5 on 2020-05-06 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrailApp', '0004_auto_20200506_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity_period',
            name='end_datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='activity_period',
            name='start_datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]