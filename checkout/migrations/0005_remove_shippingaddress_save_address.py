# Generated by Django 2.2.6 on 2019-10-19 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_shippingaddress_save_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='save_address',
        ),
    ]
