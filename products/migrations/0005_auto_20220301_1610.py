# Generated by Django 3.0.3 on 2022-03-01 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20220301_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
