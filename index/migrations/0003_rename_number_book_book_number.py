# Generated by Django 3.2.6 on 2021-08-24 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20210824_1144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='number',
            new_name='book_number',
        ),
    ]
