from django.core.management.base import BaseCommand
from ecommerce.factories import CategoryFactory, ProductFactory


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = CategoryFactory.create_batch(5)

        for category in categories:
            products = ProductFactory.create_batch(6, category=category)
            for product in products:
                product.image = "image.webp"
                product.save()

            self.stdout.write(
                self.style.SUCCESS(
                    "Successfully populated the database with test data."
                )
            )
