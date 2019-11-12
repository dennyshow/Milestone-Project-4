from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=45, default='')
    product_description = models.CharField(max_length=45)
    product_history = models.TextField()
    product_image = models.ImageField(upload_to='images')
    product_quantity = models.IntegerField()
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    product_reviews = models.TextField(max_length=248)
    
    
    def __str__(self):
        return str(self.product_name)