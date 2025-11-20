from django.contrib import admin
from .models import ProductCategory, Product, ProductImage, MarketplaceSettings


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    max_num = 4


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_active', 'position', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['position', 'name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'mrp', 'selling_price', 'discount_percentage', 'is_active', 'is_featured', 'stock_quantity', 'created_at']
    list_filter = ['category', 'is_active', 'is_featured', 'is_in_stock', 'created_at']
    search_fields = ['title', 'description', 'sku']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductImageInline]
    readonly_fields = ['sku', 'discount_percentage', 'created_at', 'updated_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'short_description', 'category')
        }),
        ('Pricing', {
            'fields': ('mrp', 'selling_price', 'discount_percentage')
        }),
        ('Product Details', {
            'fields': ('sku', 'weight', 'unit')
        }),
        ('Stock Management', {
            'fields': ('stock_quantity', 'is_in_stock', 'low_stock_threshold')
        }),
        ('Status & Features', {
            'fields': ('is_active', 'is_featured')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'position', 'is_primary', 'created_at']
    list_filter = ['is_primary', 'created_at']
    search_fields = ['product__title', 'alt_text']


@admin.register(MarketplaceSettings)
class MarketplaceSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Only allow one instance
        return not MarketplaceSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Don't allow deletion
        return False
    
    fieldsets = (
        ('WhatsApp Configuration', {
            'fields': ('whatsapp_number', 'whatsapp_message_template')
        }),
        ('Currency Settings', {
            'fields': ('currency_symbol', 'currency_code')
        }),
        ('Stock Management', {
            'fields': ('enable_stock_management', 'show_out_of_stock_products')
        }),
    )
