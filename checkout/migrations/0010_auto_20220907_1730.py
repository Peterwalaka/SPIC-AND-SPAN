# Generated by Django 2.2.10 on 2022-09-07 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0009_auto_20220907_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='approval',
            field=models.BooleanField(default=False, verbose_name='approved'),
        ),
    ]
