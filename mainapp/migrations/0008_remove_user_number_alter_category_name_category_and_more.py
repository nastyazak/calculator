# Generated by Django 4.2.1 on 2023-06-06 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_typework_hours'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='number',
        ),
        migrations.AlterField(
            model_name='category',
            name='name_category',
            field=models.CharField(max_length=100, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=11, verbose_name='Номер телефона'),
        ),
    ]
