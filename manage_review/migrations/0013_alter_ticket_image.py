# Generated by Django 5.0 on 2023-12-15 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_review', '0012_alter_ticket_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='image',
            field=models.ImageField(default='', upload_to='static//images/'),
        ),
    ]
