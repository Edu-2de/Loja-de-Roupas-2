from django import forms
from .models import Produto, Marca, Banner

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'marca', 'preco', 'categoria', 'genero']

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nome', 'cor', 'logo']

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['foto', 'marca']
