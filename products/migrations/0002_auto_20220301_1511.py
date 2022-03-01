# Generated by Django 3.0.3 on 2022-03-01 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='status',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.URLField(default='https://www.datocms-assets.com/45470/1631795624-logo-django.png%27', verbose_name='Produit image, url'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default='0', verbose_name='Enter price'),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default='0', verbose_name='Produit quantity'),
        ),
    ]