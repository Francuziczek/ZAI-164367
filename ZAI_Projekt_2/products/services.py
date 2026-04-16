import requests
from .models import Product

API_URL = "https://fakestoreapi.com/products"

def fetch_products():
    response = requests.get(API_URL)
    return response.json()

def save_products(data):
    for item in data:
        Product.objects.update_or_create(
            title=item['title'],
            defaults={
                'price': item['price'],
                'description': item['description'],
                'category': item['category'],
                'image': item['image']
            }
        )