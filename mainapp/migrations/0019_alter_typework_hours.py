# Generated by Django 4.2.1 on 2023-06-10 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_typework_price_alter_order_id_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typework',
            name='hours',
            field=models.IntegerField(default=1, verbose_name='Трудозатраты'),
        ),
    ]
