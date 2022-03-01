from django.db import models


class Product(models.Model):
    name = models.CharField(verbose_name="Product name", max_length=65, unique=True)
    quantity = models.IntegerField()
    price = models.IntegerField()
    image = models.URLField(verbose_name="Produit image, url", default='https://www.datocms-assets.com/45470/1631795624-logo-django.png')

    def __str__(self):
        return self.name