# Generated by Django 2.2.10 on 2022-09-05 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20220905_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='phone',
            field=models.IntegerField(max_length=10),
        ),
    ]
