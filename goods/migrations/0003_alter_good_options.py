# Generated by Django 5.0.2 on 2024-02-09 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_alter_good_image_alter_good_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='good',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]