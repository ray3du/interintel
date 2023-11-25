from django.test import TestCase
from ecommerce.models import Product
from django.urls import reverse

# Create your tests here.
class SearchTest(TestCase):
    def setUp(self) -> None:
        self.product1 = Product.objects.create(name='Product 1')
        self.product2 = Product.objects.create(name='Product 2')
        self.product3 = Product.objects.create(name='Product 3')
        self.iphone = Product.objects.create(name='Iphone 1')
        self.iphone = Product.objects.create(name='Iphone X')

    def test_search(self):
        response = self.client.get(reverse('ecommerce:home'), {'action': 'search_data', 'q': 'Product'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Product 1')
        self.assertContains(response, 'Product 2')
        self.assertContains(response, 'Product 3')

        response = self.client.get(reverse('ecommerce:home'), {'action': 'search_data', 'q': 'Iphone'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Iphone 1')
        self.assertContains(response, 'Iphone X')




