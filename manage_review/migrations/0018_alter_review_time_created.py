# Generated by Django 5.0 on 2023-12-28 08:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_review', '0017_alter_review_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='time_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
