# Generated by Django 5.0.2 on 2024-02-09 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0006_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.IntegerField(choices=[('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1'), ('0', '0')], default=5, verbose_name='Оценка'),
        ),
    ]
