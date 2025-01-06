from django.shortcuts import render, redirect
from .forms import ProdutoForm, MarcaForm, BannerForm, CategoriaForm
from .models import Produto, Marca, Banner
from random import choice
from datetime import datetime, timedelta
from django.core.cache import cache

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
    produtos_marca_semana = Produto.objects.filter(marca=marca_semana).order_by('-id')[:5]

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


