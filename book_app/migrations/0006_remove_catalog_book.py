# Generated by Django 4.2.7 on 2023-11-05 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0005_alter_catalog_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalog',
            name='book',
        ),
    ]
