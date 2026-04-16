from django.core.management.base import BaseCommand
from products.services import fetch_products, save_products

class Command(BaseCommand):
    help = 'Import produktów z API'

    def handle(self, *args, **kwargs):
        data = fetch_products()
        save_products(data)
        self.stdout.write(self.style.SUCCESS('Produkty zaimportowane'))
