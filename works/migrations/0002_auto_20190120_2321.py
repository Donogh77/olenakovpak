# Generated by Django 2.0.6 on 2019-01-20 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]