# Generated by Django 2.1.4 on 2019-01-10 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
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
