from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, import_products, product_page

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('import/', import_products),
    path('page/', product_page),
]