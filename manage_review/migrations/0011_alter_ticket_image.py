# Generated by Django 5.0 on 2023-12-14 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_review', '0010_alter_ticket_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]