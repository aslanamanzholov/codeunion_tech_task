# Generated by Django 4.2.7 on 2023-11-04 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название валюты'),
        ),
        migrations.AlterField(
            model_name='currency',
            name='rate',
            field=models.DecimalField(decimal_places=2, max_digits=10, max_length=255, verbose_name='Курс валюты к KZT'),
        ),
    ]
