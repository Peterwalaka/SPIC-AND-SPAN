# Generated by Django 2.2.10 on 2022-09-28 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_order_approval'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='approval',
        ),
    ]
