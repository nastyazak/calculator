# Generated by Django 4.2.1 on 2023-06-08 00:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_userchoice_remove_ordersworks_id_orders_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrdersWorks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_orders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.orders')),
                ('id_works', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.typework')),
            ],
        ),
        migrations.DeleteModel(
            name='UserChoice',
        ),
    ]
