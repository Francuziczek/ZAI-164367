from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.shortcuts import render
from .services import fetch_products, save_products


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    search_fields = ['title', 'description']
    ordering_fields = ['price']
    permission_classes = [IsAuthenticatedOrReadOnly]


@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def import_products(request):
    data = fetch_products()
    save_products(data)
    return Response({"status": "Zaimportowano"})

def product_page(request):
    return render(request, 'products.html')
