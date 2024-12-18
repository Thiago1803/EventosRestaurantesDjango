# Generated by Django 5.1.3 on 2024-11-26 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
            ],
        ),
        migrations.AddField(
            model_name='restaurants',
            name='category',
            field=models.CharField(default='Sem Categoria', max_length=150, verbose_name='Categoria'),
        ),
        migrations.AddField(
            model_name='restaurants',
            name='city',
            field=models.CharField(default='null', max_length=150, verbose_name='Cidade'),
        ),
        migrations.AddField(
            model_name='restaurants',
            name='menu',
            field=models.ManyToManyField(related_name='restaurants', to='restaurants.food'),
        ),
    ]
