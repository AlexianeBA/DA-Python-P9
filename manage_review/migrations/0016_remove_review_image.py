# Generated by Django 5.0 on 2023-12-21 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_review', '0015_review_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='image',
        ),
    ]