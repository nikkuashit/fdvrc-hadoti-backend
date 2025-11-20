from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from slugify import slugify
import uuid


class ProductCategory(models.Model):
    """Product categories for marketplace items"""
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    icon = models.FileField(upload_to='marketplace/categories/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    position = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(ProductCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Product Categories"
        ordering = ['position', 'name']


class Product(models.Model):
    """Marketplace products"""
    # Basic Info
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    short_description = models.CharField(max_length=500, blank=True)

    # Category
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        related_name='products'
    )

    # Pricing (in INR)
    mrp = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text="Maximum Retail Price in INR"
    )
    selling_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text="Selling Price in INR"
    )
    discount_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    # Product Details
    sku = models.CharField(max_length=100, unique=True, blank=True, help_text="Stock Keeping Unit")
    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Weight in kg")
    unit = models.CharField(max_length=50, default='piece', help_text="Unit of measurement (kg, piece, pack, etc.)")

    # Stock (for future e-commerce)
    stock_quantity = models.IntegerField(default=0)
    is_in_stock = models.BooleanField(default=True)
    low_stock_threshold = models.IntegerField(default=5)

    # Status
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    # SEO
    meta_title = models.CharField(max_length=255, blank=True)
    meta_description = models.TextField(blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Auto-generate slug if not provided
        if not self.slug:
            base_slug = slugify(self.title)
            self.slug = f"{base_slug}-{str(uuid.uuid4())[:8]}"

        # Auto-generate SKU if not provided
        if not self.sku:
            self.sku = f"PRD-{str(uuid.uuid4())[:8].upper()}"

        # Calculate discount percentage if not set
        if self.mrp and self.selling_price and self.discount_percentage == 0:
            if self.mrp > self.selling_price:
                self.discount_percentage = ((self.mrp - self.selling_price) / self.mrp) * 100

        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def discount_amount(self):
        """Calculate discount amount in INR"""
        return self.mrp - self.selling_price

    @property
    def primary_image(self):
        """Get the primary product image"""
        primary = self.images.filter(is_primary=True).first()
        return primary if primary else self.images.first()

    class Meta:
        verbose_name_plural = "Products"
        ordering = ['-created_at']


class ProductImage(models.Model):
    """Product images (max 4 per product)"""
    product = models.ForeignKey(
        Product,
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.FileField(upload_to='marketplace/products/')
    position = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(3)],
        help_text="Position 0-3 (max 4 images)"
    )
    is_primary = models.BooleanField(default=False)
    alt_text = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Ensure only one primary image per product
        if self.is_primary:
            ProductImage.objects.filter(
                product=self.product,
                is_primary=True
            ).update(is_primary=False)
        super(ProductImage, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.title} - Image {self.position + 1}"

    class Meta:
        ordering = ['position']
        unique_together = ['product', 'position']


class MarketplaceSettings(models.Model):
    """Global marketplace settings"""
    whatsapp_number = models.CharField(
        max_length=15,
        default='919424144355',
        help_text="WhatsApp business number with country code (e.g., 919424144355)"
    )
    whatsapp_message_template = models.TextField(
        default="Hi! I'm interested in: {product_title}\nPrice: ₹{selling_price}\nProduct Link: {product_url}",
        help_text="Use {product_title}, {selling_price}, {product_url} as placeholders"
    )
    currency_symbol = models.CharField(max_length=5, default='₹')
    currency_code = models.CharField(max_length=3, default='INR')
    enable_stock_management = models.BooleanField(default=False)
    show_out_of_stock_products = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Marketplace Settings"

    class Meta:
        verbose_name = "Marketplace Settings"
        verbose_name_plural = "Marketplace Settings"

    def save(self, *args, **kwargs):
        # Ensure only one settings instance exists
        self.pk = 1
        super(MarketplaceSettings, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        """Load or create settings"""
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
