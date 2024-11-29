# Generated by Django 5.1.3 on 2024-11-29 01:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_restaurants_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurants',
            name='total_resevations',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Total de Vagas'),
        ),
    ]