from django.shortcuts import render, redirect
from .forms import ProdutoForm, MarcaForm, BannerForm, CategoriaForm, LoginForm, RegisterForm
from .models import Produto, Marca, Banner
from random import choice
from datetime import datetime, timedelta
from django.core.cache import cache
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group

# Create your views here.
def home(request):
    marcas = Marca.objects.all()
    banners = Banner.objects.all().order_by('-id')[:3]
    produtos = Produto.objects.all().order_by('-id')[:10]

    # Lógica para marca da semana
    CACHE_KEY = 'marca_semana'
    marca_semana = cache.get(CACHE_KEY)
    
    if marca_semana is None:
        # Se não houver marca em cache, seleciona uma nova
        todas_marcas = list(Marca.objects.all())
        if todas_marcas:
            marca_semana = choice(todas_marcas)
            # Cache por 7 dias
            cache.set(CACHE_KEY, marca_semana.id, 60*60*24*7)
    else:
        marca_semana = Marca.objects.get(id=marca_semana)

    # Pega os últimos produtos da marca selecionada
    # Primeiro, pegamos os IDs dos produtos novidades
    produtos_novidades_ids = set(produtos.values_list('id', flat=True))
    
    # Depois, filtramos os produtos da marca excluindo os IDs das novidades
    produtos_marca_semana = (Produto.objects
                           .filter(marca=marca_semana)
                           .exclude(id__in=produtos_novidades_ids)
                           .order_by('-id')[:5])

    return render(request, 'index.html', {
        'marcas': marcas,
        'banners': banners,
        'produtos': produtos,
        'marca_semana': marca_semana,
        'produtos_marca_semana': produtos_marca_semana,
    })


def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redireciona para a página inicial após salvar
    else:
        form = ProdutoForm()
    
    return render(request, 'criar_produto.html', {'form': form})


def criar_marca(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MarcaForm()
    
    return render(request, 'criar_marca.html', {'form': form})


def criar_banner(request):
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BannerForm()
    
    return render(request, 'criar_banner.html', {'form': form})


def criar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoriaForm()
    
    return render(request, 'criar_categoria.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Adiciona o usuário ao grupo 'Usuario'
            grupo_usuario = Group.objects.get_or_create(name='Usuario')[0]
            user.groups.add(grupo_usuario)
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


# Decorator para verificar se o usuário é admin
def is_admin(user):
    return user.groups.filter(name='Admin').exists()


# View protegida que só pode ser acessada por admins
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


# View protegida que só pode ser acessada por usuários logados
@login_required
def user_profile(request):
    return render(request, 'user_profile.html')


