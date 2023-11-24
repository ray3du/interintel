from uuid import uuid4

from django.db import models


def image_path(instance, filename):
    unique_filename = f"{uuid4()}.{filename}"
    return f"products/{unique_filename}"


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50, blank=True, default="")
    price = models.CharField(max_length=100)
    category = models.ForeignKey('ecommerce.Category', null=True, blank=True, on_delete=models.CASCADE, related_name='products')
    description = models.TextField()
    image = models.ImageField(upload_to=image_path)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Product'


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Category'


"""
class CartItems(models.Model):
    product = models.ForeignKey('ecommerce.Product', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.product.name} - Qty({self.qty})"
    

class Cart(models.Model):
    items = models.ManyToManyField(to='ecommerce.CartItems')
"""
