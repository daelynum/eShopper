import json
from django.core.management import BaseCommand

from authapp.models import User
from mainapp.models import ProductCategory, Product


def load_from_json(file_name):
    with open(file_name, mode='r', encoding='utf-8') as in_file:
        return json.load(in_file)

class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.create_superuser(username='vladimir', email='admin@mail.ru', password='1')

        categories = load_from_json('/Users/vladimirivanov/Documents/eShopper/eShopper/mainapp/fixtures/category.json')

        ProductCategory.objects.all().delete()
        for category in categories:
            cat = category.get('fields')
            cat['id'] = category.get('pk')
            new_category = ProductCategory(**cat)
            new_category.save()

        products = load_from_json('/Users/vladimirivanov/Documents/eShopper/eShopper/mainapp/fixtures/products.json')

        Product.objects.all().delete()
        for product in products:
            prod = product.get('fields')
            category = prod.get('category')
            _category = ProductCategory.objects.get(id=category)
            prod['category'] = _category
            new_category = Product(**prod)
            new_category.save()