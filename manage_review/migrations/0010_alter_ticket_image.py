# Generated by Django 5.0 on 2023-12-14 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_review', '0009_alter_ticket_uploader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
