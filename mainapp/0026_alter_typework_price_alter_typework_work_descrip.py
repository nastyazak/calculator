# Generated by Django 4.2.1 on 2023-06-15 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0025_remove_typework_name_work_estimate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typework',
            name='price',
            field=models.IntegerField(verbose_name='Стоимость нормо-часа'),
        ),
        migrations.AlterField(
            model_name='typework',
            name='work_descrip',
            field=models.TextField(verbose_name='Описание работы'),
        ),
    ]
