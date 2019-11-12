from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductTest(TestCase):
    def test_str(self):
        test_product_name = Product(product_name='A product')
        self.assertEqual(str(test_product_name), 'A product')