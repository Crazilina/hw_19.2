# Generated by Django 5.0.3 on 2024-04-23 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_blogpost_remove_product_manufactured_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'verbose_name': 'Запись', 'verbose_name_plural': 'Записи'},
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(max_length=200, unique=True, verbose_name='Slug'),
        ),
    ]
