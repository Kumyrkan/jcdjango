# Generated by Django 5.0.2 on 2024-02-09 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='num_ord',
            field=models.IntegerField(default=0, verbose_name='Номер заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена'),
        ),
    ]
