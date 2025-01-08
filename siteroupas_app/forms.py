from django import forms
from .models import Product, Brand, Banner, Category, Color
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'gender', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }

    brands = forms.ModelMultipleChoiceField(
        queryset=Brand.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-select'})
    )

    colors = forms.ModelMultipleChoiceField(
        queryset=Color.objects.all(),
        widget=forms.SelectMultiple(attrs={
            'class': 'form-select',
            'data-color-picker': 'true'
        })
    )
    for option in colors.queryset:
        colors.widget.attrs['data-color-code' + str(option.id)] = option.get_color_code()

    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-select'})
    )


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'logo']

    colors = forms.ModelMultipleChoiceField(
        queryset=Color.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-select'})
    )

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['photo', 'brand']


class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ['name', 'code']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)