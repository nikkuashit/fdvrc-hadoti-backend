from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from hadoti_backend.permissions import IsAdminOrStaffOrReadOnly
from .models import ProductCategory, Product, ProductImage, MarketplaceSettings
from .serializers import (
    ProductCategorySerializer, ProductListSerializer,
    ProductDetailSerializer, ProductImageSerializer,
    MarketplaceSettingsSerializer
)


class ProductCategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for product categories"""
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = [IsAdminOrStaffOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active']
    search_fields = ['name', 'description']
    ordering_fields = ['position', 'name', 'created_at']
    ordering = ['position', 'name']
    lookup_field = 'slug'


class ProductViewSet(viewsets.ModelViewSet):
    """ViewSet for products"""
    queryset = Product.objects.prefetch_related('images', 'category')
    permission_classes = [IsAdminOrStaffOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'is_active', 'is_featured', 'is_in_stock']
    search_fields = ['title', 'description', 'short_description', 'sku']
    ordering_fields = ['created_at', 'mrp', 'selling_price', 'title']
    ordering = ['-created_at']
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return ProductDetailSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # For non-authenticated users, only show active products
        if not self.request.user.is_authenticated:
            queryset = queryset.filter(is_active=True)
        return queryset

    @action(detail=True, methods=['post'], permission_classes=[IsAdminOrStaffOrReadOnly])
    def upload_image(self, request, slug=None):
        """Upload image for a product"""
        product = self.get_object()
        
        # Check if product already has 4 images
        existing_images = product.images.count()
        if existing_images >= 4:
            return Response(
                {'error': 'Maximum 4 images allowed per product'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = ProductImageSerializer(data=request.data)
        if serializer.is_valid():
            # Find next available position
            used_positions = list(product.images.values_list('position', flat=True))
            position = 0
            while position in used_positions and position < 4:
                position += 1
            
            serializer.save(product=product, position=position)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductImageViewSet(viewsets.ModelViewSet):
    """ViewSet for product images"""
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [IsAdminOrStaffOrReadOnly]


class MarketplaceSettingsViewSet(viewsets.ViewSet):
    """ViewSet for marketplace settings (singleton)"""
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request):
        """Get marketplace settings"""
        settings = MarketplaceSettings.load()
        serializer = MarketplaceSettingsSerializer(settings)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        """Update marketplace settings"""
        if not request.user.is_staff:
            return Response(
                {'error': 'Only staff can update settings'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        settings = MarketplaceSettings.load()
        serializer = MarketplaceSettingsSerializer(settings, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
