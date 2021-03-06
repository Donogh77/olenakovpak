# Generated by Django 2.1.4 on 2019-01-02 16:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190102_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='is_image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
