# Generated by Django 4.2.1 on 2023-06-07 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_alter_ordersworks_id_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordersworks',
            name='id_orders',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.orders'),
        ),
    ]
