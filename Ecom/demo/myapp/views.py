from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Category, Product, Order, OrderItem
from .cart import Cart
from django.contrib.auth.models import User


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        
    return render(request, 'myapp/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'myapp/product/detail.html', {'product': product})


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'myapp/cart/detail.html', {'cart': cart})


def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=1, override_quantity=False)
    return redirect('myapp:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('myapp:cart_detail')


def checkout(request):
    cart = Cart(request)
    if request.method == 'POST':
        # Process checkout form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal_code')
        country = request.POST.get('country')
        
        # Create order
        order = Order(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            address=address,
            city=city,
            postal_code=postal_code,
            country=country
        )
        
        # If user is authenticated, associate with user
        if request.user.is_authenticated:
            order.user = request.user
            
        order.save()
        
        # Create order items
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )
            
        # Clear the cart
        cart.clear()
        
        # Redirect to order confirmation
        return render(request, 'myapp/checkout/confirmation.html', {'order': order})
    
    return render(request, 'myapp/checkout/checkout.html', {'cart': cart})


@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        # Process order creation for authenticated users
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal_code')
        country = request.POST.get('country')
        
        # Create order
        order = Order(
            user=request.user,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            address=address,
            city=city,
            postal_code=postal_code,
            country=country
        )
        order.save()
        
        # Create order items
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )
            
        # Clear the cart
        cart.clear()
        
        # Redirect to order confirmation
        return render(request, 'myapp/checkout/confirmation.html', {'order': order})
    
    return render(request, 'myapp/checkout/create.html', {'cart': cart})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('myapp:product_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
