from django.urls import path, include
from rest_framework import routers
from .views import (
    ProductCategoryViewSet, ProductViewSet,
    ProductImageViewSet, MarketplaceSettingsViewSet
)

router = routers.DefaultRouter()
router.register('categories', ProductCategoryViewSet)
router.register('products', ProductViewSet)
router.register('product-images', ProductImageViewSet)
router.register('settings', MarketplaceSettingsViewSet, basename='marketplace-settings')

urlpatterns = [
    path('', include(router.urls)),
]
