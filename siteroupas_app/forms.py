from django import forms
from .models import Produto, Marca, Banner, Categoria

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'marca', 'preco', 'categoria', 'genero', 'foto']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-select'}),
            'preco': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'genero': forms.Select(attrs={'class': 'form-select'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nome', 'cor', 'logo']

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['foto', 'marca']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
