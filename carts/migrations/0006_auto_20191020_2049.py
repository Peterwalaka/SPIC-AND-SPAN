# Generated by Django 2.2.6 on 2019-10-20 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_promotioncode'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PromotionCode',
        ),
        migrations.AddField(
            model_name='order',
            name='promo_code_applied',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='promo_code_discount',
            field=models.FloatField(default=0),
        ),
    ]