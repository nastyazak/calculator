# Generated by Django 4.2.1 on 2023-06-10 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_rename_order_orders_rename_orderwork_orderworks'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
        migrations.RenameModel(
            old_name='OrderWorks',
            new_name='OrderWork',
        ),
    ]
