# Generated by Django 5.0.2 on 2024-02-09 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='good',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена'),
        ),
    ]
