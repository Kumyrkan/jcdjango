# Generated by Django 5.0.2 on 2024-02-10 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0009_alter_good_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('pk',), 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]