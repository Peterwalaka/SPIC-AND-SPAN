# Generated by Django 2.2.10 on 2022-09-28 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='approval',
            field=models.BooleanField(default=False, verbose_name='approval'),
        ),
    ]
