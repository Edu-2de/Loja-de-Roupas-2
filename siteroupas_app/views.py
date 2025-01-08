from django.shortcuts import render, redirect
from .forms import ProductForm, BrandForm, BannerForm, CategoryForm, ColorForm, LoginForm, RegisterForm
from .models import Product, Brand, Banner
from random import choice
from datetime import datetime, timedelta
from django.core.cache import cache
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group

# Create your views here.
def home(request):
    brands = Brand.objects.all()
    banners = Banner.objects.all().order_by('-id')[:3]
    products = Product.objects.all().order_by('-id')[:10]

    # Logic for brand of the week
    CACHE_KEY = 'brand_of_the_week'
    brand_of_the_week = cache.get(CACHE_KEY)
    
    if brand_of_the_week is None:
        # If there is no brand in cache, select a new one
        all_brands = list(Brand.objects.all())
        if all_brands:
            brand_of_the_week = choice(all_brands)
            # Cache for 7 days
            cache.set(CACHE_KEY, brand_of_the_week.id, 60*60*24*7)
    else:
        brand_of_the_week = Brand.objects.get(id=brand_of_the_week)

    # Get the latest products of the selected brand
    # First, we get the IDs of the new products
    new_products_ids = set(products.values_list('id', flat=True))
    
    # Then, we filter the products of the brand excluding the IDs of the new products
    brand_of_the_week_products = (Product.objects
                               .filter(brand=brand_of_the_week)
                               .exclude(id__in=new_products_ids)
                               .order_by('-id')[:5])

    return render(request, 'index.html', {
        'brands': brands,
        'banners': banners,
        'products': products,
        'brand_of_the_week': brand_of_the_week,
        'brand_of_the_week_products': brand_of_the_week_products,
    })


def create_product(request):
    """
    View to create a new product.

    This view is accessed when the user navigates to the 'create_product' URL.
    It renders a form to input the product details.
    After the form is submitted, the product is saved to the database and the user is redirected to the home page.
    """
    if request.method == 'POST':
        # Create a form instance with the submitted data and files
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            # Redirect to the home page after saving
            return redirect('home')
    else:
        # Create an empty form instance
        form = ProductForm()
    
    # Render the create_product template with the form
    return render(request, 'create_product.html', {'form': form})


def create_brand(request):
    """
    View to create a new brand.

    This view is accessed when the user navigates to the 'create_brand' URL.
    It renders a form to input the brand's name and logo.
    After the form is submitted, the brand is saved to the database and the user is redirected to the home page.
    """
    if request.method == 'POST':
        # Create a form with the POST data
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form and redirect to the home page
            form.save()
            return redirect('home')
    else:
        # Create an empty form
        form = BrandForm()
    
    # Render the form in the 'create_brand.html' template
    return render(request, 'create_brand.html', {'form': form})


def create_banner(request):
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BannerForm()
    
    return render(request, 'create_banner.html', {'form': form})


def create_color(request):
    if request.method == 'POST':
        form = ColorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ColorForm()
    
    return render(request, 'create_color.html', {'form': form})

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
    
    return render(request, 'create_category.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Add the user to the 'User' group
            user_group = Group.objects.get_or_create(name='User')[0]
            user.groups.add(user_group)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


# Decorator to check if the user is an admin
def is_admin(user):
    return user.groups.filter(name='Admin').exists()


# View protected by the is_admin decorator
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


# View protected by the login_required decorator
@login_required
def user_profile(request):
    return render(request, 'user_profile.html')