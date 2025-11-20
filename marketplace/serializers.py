from rest_framework import serializers
from .models import ProductCategory, Product, ProductImage, MarketplaceSettings


class ProductImageSerializer(serializers.ModelSerializer):
    """Serializer for product images"""

    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'position', 'is_primary', 'alt_text', 'created_at']
        read_only_fields = ['id', 'created_at']


class ProductCategorySerializer(serializers.ModelSerializer):
    """Serializer for product categories"""
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'slug', 'description', 'icon', 'is_active', 'position', 'product_count', 'created_at', 'updated_at']
        read_only_fields = ['id', 'slug', 'created_at', 'updated_at']

    def get_product_count(self, obj):
        return obj.products.filter(is_active=True).count()


class ProductListSerializer(serializers.ModelSerializer):
    """Serializer for product list view"""
    category_name = serializers.CharField(source='category.name', read_only=True)
    primary_image = serializers.SerializerMethodField()
    discount_amount = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'title', 'slug', 'short_description', 'category_name',
            'mrp', 'selling_price', 'discount_percentage', 'discount_amount',
            'primary_image', 'is_in_stock', 'is_featured', 'created_at'
        ]
        read_only_fields = ['id', 'slug', 'discount_amount', 'created_at']

    def get_primary_image(self, obj):
        primary = obj.primary_image
        if primary:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(primary.image.url)
        return None


class ProductDetailSerializer(serializers.ModelSerializer):
    """Serializer for product detail view"""
    category = ProductCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=ProductCategory.objects.all(),
        source='category',
        write_only=True
    )
    images = ProductImageSerializer(many=True, read_only=True)
    discount_amount = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'title', 'slug', 'description', 'short_description',
            'category', 'category_id', 'mrp', 'selling_price',
            'discount_percentage', 'discount_amount', 'sku', 'weight', 'unit',
            'stock_quantity', 'is_in_stock', 'low_stock_threshold',
            'is_active', 'is_featured', 'meta_title', 'meta_description',
            'images', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'slug', 'sku', 'discount_amount', 'created_at', 'updated_at']


class MarketplaceSettingsSerializer(serializers.ModelSerializer):
    """Serializer for marketplace settings"""

    class Meta:
        model = MarketplaceSettings
        fields = [
            'whatsapp_number', 'whatsapp_message_template',
            'currency_symbol', 'currency_code', 'enable_stock_management',
            'show_out_of_stock_products', 'updated_at'
        ]
        read_only_fields = ['updated_at']
