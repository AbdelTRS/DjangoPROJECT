# Generated by Django 3.0.3 on 2022-03-01 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20220301_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.URLField(default='https://www.backmarket.fr/cdn-cgi/image/format=auto,quality=75,width=640/https://d1eh9yux7w8iql.cloudfront.net/product_images/347039_04dd59af-c59a-42e5-9278-8cb7b7a8cb9a.jpg', verbose_name='Produit image, url'),
        ),
    ]
