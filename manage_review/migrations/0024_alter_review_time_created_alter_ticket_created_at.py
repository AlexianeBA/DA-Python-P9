# Generated by Django 5.0 on 2024-01-04 13:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_review', '0023_alter_review_time_created_alter_ticket_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 13, 58, 1, 233620)),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 13, 58, 1, 233275)),
        ),
    ]
