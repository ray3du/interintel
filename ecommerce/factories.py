import factory
from factory.django import DjangoModelFactory
from .models import Category, Product


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("word")


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker("word")
    description = factory.Faker("paragraph")
    price = factory.Faker("pydecimal", left_digits=3, right_digits=2)
