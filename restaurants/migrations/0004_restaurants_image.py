# Generated by Django 5.1.3 on 2024-11-26 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_category_alter_food_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurants',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='restaurants/', verbose_name='Imagem'),
        ),
    ]