# Generated by Django 5.0 on 2023-12-18 14:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_review', '0013_alter_ticket_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
