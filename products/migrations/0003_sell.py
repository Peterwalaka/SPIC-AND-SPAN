# Generated by Django 2.2.10 on 2022-04-05 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20191020_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='sells/')),
                ('location', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('negotiable', models.BooleanField()),
                ('phone_number', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Category')),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
    ]