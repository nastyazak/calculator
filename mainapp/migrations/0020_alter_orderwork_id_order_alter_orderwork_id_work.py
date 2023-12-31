# Generated by Django 4.2.1 on 2023-06-10 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_alter_typework_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderwork',
            name='id_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.order', verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='orderwork',
            name='id_work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.typework', verbose_name='Работа'),
        ),
    ]
