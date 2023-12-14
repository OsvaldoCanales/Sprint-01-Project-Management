# Generated by Django 4.2.8 on 2023-12-14 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0028_remove_member_catalog_alter_catalog_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='catalog',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='book_app.catalog'),
        ),
    ]
