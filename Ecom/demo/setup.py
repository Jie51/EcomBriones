#!/usr/bin/env python
"""
Setup script for the Ecommerce Website.
This script creates a superuser and sample data for testing.
"""

import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
django.setup()

from django.contrib.auth.models import User
from myapp.models import Category, Product

def create_superuser():
    """Create a superuser for admin access."""
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("Superuser 'admin' created successfully!")
        print("Username: admin")
        print("Password: admin123")
    else:
        print("Superuser 'admin' already exists!")

def create_sample_data():
    """Create sample categories and products for testing."""
    # Create sample categories
    categories_data = [
        {'name': 'Electronics', 'slug': 'electronics', 'description': 'Electronic devices and gadgets'},
        {'name': 'Clothing', 'slug': 'clothing', 'description': 'Apparel and fashion items'},
        {'name': 'Books', 'slug': 'books', 'description': 'Books and literature'},
        {'name': 'Home & Garden', 'slug': 'home-garden', 'description': 'Home improvement and garden supplies'},
    ]

    # Create categories
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            slug=cat_data['slug'],
            defaults={
                'name': cat_data['name'],
                'description': cat_data['description']
            }
        )
        if created:
            print(f"Created category: {category.name}")
        else:
            print(f"Category already exists: {category.name}")

    # Create sample products
    products_data = [
        {
            'category_slug': 'electronics',
            'name': 'Smartphone',
            'slug': 'smartphone',
            'description': 'Latest model smartphone with advanced features',
            'price': 699.99,
            'stock': 50,
            'available': True
        },
        {
            'category_slug': 'electronics',
            'name': 'Laptop',
            'slug': 'laptop',
            'description': 'High-performance laptop for work and gaming',
            'price': 1299.99,
            'stock': 25,
            'available': True
        },
        {
            'category_slug': 'clothing',
            'name': 'T-Shirt',
            'slug': 't-shirt',
            'description': 'Comfortable cotton t-shirt',
            'price': 19.99,
            'stock': 100,
            'available': True
        },
        {
            'category_slug': 'clothing',
            'name': 'Jeans',
            'slug': 'jeans',
            'description': 'Stylish denim jeans',
            'price': 49.99,
            'stock': 75,
            'available': True
        },
        {
            'category_slug': 'books',
            'name': 'Python Programming',
            'slug': 'python-programming',
            'description': 'Learn Python programming from beginner to expert',
            'price': 29.99,
            'stock': 30,
            'available': True
        },
        {
            'category_slug': 'home-garden',
            'name': 'Garden Tools Set',
            'slug': 'garden-tools-set',
            'description': 'Complete set of gardening tools',
            'price': 89.99,
            'stock': 20,
            'available': True
        },
    ]

    # Create products
    for prod_data in products_data:
        try:
            category = Category.objects.get(slug=prod_data['category_slug'])
            product, created = Product.objects.get_or_create(
                slug=prod_data['slug'],
                defaults={
                    'category': category,
                    'name': prod_data['name'],
                    'description': prod_data['description'],
                    'price': prod_data['price'],
                    'stock': prod_data['stock'],
                    'available': prod_data['available']
                }
            )
            if created:
                print(f"Created product: {product.name}")
            else:
                print(f"Product already exists: {product.name}")
        except Category.DoesNotExist:
            print(f"Category {prod_data['category_slug']} does not exist!")

    print("Sample data population completed!")

def main():
    """Main function to run setup."""
    print("Setting up Ecommerce Website...")
    create_superuser()
    create_sample_data()
    print("\nSetup completed successfully!")
    print("\nTo run the application:")
    print("1. Run: python manage.py runserver")
    print("2. Visit: http://127.0.0.1:8000/")
    print("3. Admin interface: http://127.0.0.1:8000/admin/")

if __name__ == "__main__":
    main()