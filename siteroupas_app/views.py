from django.shortcuts import render, redirect
from .forms import ProdutoForm, MarcaForm, BannerForm
from .models import Produto, Marca, Banner

# Create your views here.
def home(request):

    marcas = Marca.objects.all()
    
    banners = Banner.objects.all()

    return render(request, 'index.html', {'marcas': marcas, 'banners': banners})


def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
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


