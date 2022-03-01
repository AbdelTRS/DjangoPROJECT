from django.db import models


class Product(models.Model):
    name = models.CharField(verbose_name="Product name", max_length=65, unique=True)
    quantity = models.IntegerField()
    price = models.IntegerField()
    image = models.URLField(verbose_name="Produit image, url", default='https://www.backmarket.fr/cdn-cgi/image/format=auto,quality=75,width=640/https://d1eh9yux7w8iql.cloudfront.net/product_images/347039_04dd59af-c59a-42e5-9278-8cb7b7a8cb9a.jpg')

    def __str__(self):
        return self.name