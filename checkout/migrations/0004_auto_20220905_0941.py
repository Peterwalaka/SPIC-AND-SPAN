# Generated by Django 2.2.10 on 2022-09-05 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20220905_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='phone',
            field=models.FloatField(max_length=10),
        ),
    ]