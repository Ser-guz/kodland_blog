# Generated by Django 3.0.9 on 2020-08-04 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='content_small',
            field=models.TextField(blank=True, max_length=150, null=True, verbose_name='Краткий обзор'),
        ),
    ]
