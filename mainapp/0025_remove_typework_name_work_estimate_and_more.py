# Generated by Django 4.2.1 on 2023-06-14 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0024_typework_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='typework',
            name='name_work_estimate',
        ),
        migrations.RemoveField(
            model_name='user',
            name='e_mail',
        ),
        migrations.AddField(
            model_name='typework',
            name='work_descrip',
            field=models.TextField(default='ОПИСАНИЕ', verbose_name='Описание работы'),
        ),
    ]