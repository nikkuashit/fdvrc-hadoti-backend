import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hadoti_backend.settings')
django.setup()

from marketplace.models import Product, ProductCategory

# Get categories
millets = ProductCategory.objects.get(slug='millets')
flour = ProductCategory.objects.get(slug='millet-flour')
snacks = ProductCategory.objects.get(slug='millet-snacks')
organic = ProductCategory.objects.get(slug='organic-products')

# Sample products
products_data = [
    {
        'title': 'Organic Pearl Millet (Bajra)',
        'category': millets,
        'description': '<p>Premium quality organic pearl millet sourced directly from local farmers in Hadoti region. Rich in protein, fiber, and essential minerals. Perfect for making rotis, khichdi, and porridge.</p><ul><li>100% Organic</li><li>No pesticides or chemicals</li><li>Naturally grown</li><li>Rich in iron and calcium</li></ul>',
        'short_description': 'Premium organic pearl millet from Hadoti region farmers',
        'mrp': 120,
        'discount_percentage': 10,
        'unit': 'kg',
        'weight': 1.0,
        'sku': 'MILLET-BAJRA-001',
        'is_featured': True,
        'is_in_stock': True,
    },
    {
        'title': 'Foxtail Millet (Kangni)',
        'category': millets,
        'description': '<p>Nutritious foxtail millet, ideal for diabetics and health-conscious individuals. Low glycemic index and high in dietary fiber.</p><ul><li>Diabetic-friendly</li><li>High fiber content</li><li>Gluten-free</li><li>Easy to digest</li></ul>',
        'short_description': 'Nutritious foxtail millet, ideal for health-conscious individuals',
        'mrp': 150,
        'discount_percentage': 15,
        'unit': 'kg',
        'weight': 1.0,
        'sku': 'MILLET-KANGNI-001',
        'is_featured': True,
        'is_in_stock': True,
    },
    {
        'title': 'Finger Millet (Ragi)',
        'category': millets,
        'description': '<p>High-calcium finger millet perfect for growing children and seniors. Excellent source of natural calcium and protein.</p><ul><li>High calcium content</li><li>Rich in amino acids</li><li>Good for bone health</li><li>Natural relaxant</li></ul>',
        'short_description': 'High-calcium finger millet perfect for all ages',
        'mrp': 130,
        'discount_percentage': 0,
        'unit': 'kg',
        'weight': 1.0,
        'sku': 'MILLET-RAGI-001',
        'is_in_stock': True,
    },
    {
        'title': 'Little Millet (Kutki)',
        'category': millets,
        'description': '<p>Versatile little millet that can replace rice in any dish. Rich in B vitamins and minerals.</p><ul><li>Rice alternative</li><li>Rich in B vitamins</li><li>Good for weight management</li><li>Quick cooking</li></ul>',
        'short_description': 'Versatile little millet, perfect rice alternative',
        'mrp': 140,
        'discount_percentage': 5,
        'unit': 'kg',
        'weight': 1.0,
        'sku': 'MILLET-KUTKI-001',
        'is_in_stock': True,
    },
    {
        'title': 'Bajra Flour (Pearl Millet Flour)',
        'category': flour,
        'description': '<p>Freshly ground pearl millet flour, perfect for making traditional rotis and bhakris. Stone-ground to preserve nutrients.</p><ul><li>Stone-ground</li><li>No additives</li><li>Fresh and pure</li><li>Traditional taste</li></ul>',
        'short_description': 'Fresh stone-ground pearl millet flour',
        'mrp': 80,
        'discount_percentage': 10,
        'unit': 'kg',
        'weight': 1.0,
        'sku': 'FLOUR-BAJRA-001',
        'is_featured': True,
        'is_in_stock': True,
    },
    {
        'title': 'Ragi Flour (Finger Millet Flour)',
        'category': flour,
        'description': '<p>Nutritious ragi flour ideal for making porridge, dosas, and health drinks. Perfect for babies and elders.</p><ul><li>High in calcium</li><li>Baby-friendly</li><li>Easy to digest</li><li>Naturally cooling</li></ul>',
        'short_description': 'Nutritious ragi flour for porridge and dosas',
        'mrp': 90,
        'discount_percentage': 12,
        'unit': 'kg',
        'weight': 1.0,
        'sku': 'FLOUR-RAGI-001',
        'is_in_stock': True,
    },
    {
        'title': 'Multi-Millet Flour Mix',
        'category': flour,
        'description': '<p>Premium blend of 5 different millets for maximum nutrition. Perfect for rotis, dosas, and baking.</p><ul><li>5 millet blend</li><li>Complete nutrition</li><li>Versatile use</li><li>Family pack</li></ul>',
        'short_description': 'Premium 5-millet blend for complete nutrition',
        'mrp': 100,
        'discount_percentage': 20,
        'unit': 'kg',
        'weight': 1.0,
        'sku': 'FLOUR-MULTI-001',
        'is_featured': True,
        'is_in_stock': True,
    },
    {
        'title': 'Millet Cookies - Assorted Flavors',
        'category': snacks,
        'description': '<p>Healthy baked millet cookies in 3 flavors - Jeera, Ajwain, and Methi. No maida, no preservatives.</p><ul><li>No maida</li><li>No preservatives</li><li>3 flavors</li><li>Baked, not fried</li></ul>',
        'short_description': 'Healthy baked millet cookies, assorted flavors',
        'mrp': 150,
        'discount_percentage': 10,
        'unit': '500g pack',
        'weight': 0.5,
        'sku': 'SNACK-COOKIE-001',
        'is_in_stock': True,
    },
    {
        'title': 'Millet Namkeen Mix',
        'category': snacks,
        'description': '<p>Crunchy millet-based namkeen mix perfect for tea time. Traditional taste with health benefits.</p><ul><li>Traditional recipe</li><li>Millet-based</li><li>Perfect for tea</li><li>Family size</li></ul>',
        'short_description': 'Crunchy traditional millet namkeen mix',
        'mrp': 80,
        'discount_percentage': 0,
        'unit': '250g',
        'weight': 0.25,
        'sku': 'SNACK-NAMKEEN-001',
        'is_in_stock': True,
    },
    {
        'title': 'Organic Millet Value Pack',
        'category': organic,
        'description': '<p>Combo pack of 4 different organic millets - Bajra, Ragi, Jowar, and Kangni. Perfect for trying all varieties.</p><ul><li>4 millet varieties</li><li>Certified organic</li><li>Value pack</li><li>Try all types</li></ul>',
        'short_description': 'Organic combo pack of 4 different millets',
        'mrp': 500,
        'discount_percentage': 25,
        'unit': '4kg (1kg each)',
        'weight': 4.0,
        'sku': 'ORG-COMBO-001',
        'is_featured': True,
        'is_in_stock': True,
    },
]

# Create products
created_count = 0
for product_data in products_data:
    # Calculate selling price
    mrp = product_data['mrp']
    discount = product_data.get('discount_percentage', 0)
    selling_price = mrp - (mrp * discount / 100) if discount > 0 else mrp

    product_data['selling_price'] = selling_price

    # Check if product already exists
    if not Product.objects.filter(sku=product_data['sku']).exists():
        product = Product.objects.create(**product_data)
        created_count += 1
        print(f'✓ Created: {product.title}')
    else:
        print(f'⊘ Skipped: {product_data["title"]} (already exists)')

print(f'\n✅ Created {created_count} new products!')
print(f'📦 Total products in database: {Product.objects.count()}')
