# Generated by Django 5.0 on 2024-03-30 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_review', '0028_review_content_alter_review_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='body',
            new_name='commentary',
        ),
    ]
