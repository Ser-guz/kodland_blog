# Generated by Django 3.0.9 on 2020-08-04 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_content_small'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='content_small',
        ),
    ]
