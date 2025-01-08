from django.db import models

# Create your models here.

class Brand(models.Model):
    # Field to store the full name of the brand.
    name = models.CharField(max_length=50)

    # New field for the logo
    logo = models.ImageField(upload_to='brands_logos/', null=True, blank=True)

    def __str__(self):
        # Returns the full name of the brand as a text representation of the object.
        return self.name





class Category(models.Model):
    # Field to store the full name of the category.
    name = models.CharField(max_length=50)

    def __str__(self):
        # Returns the full name of the category as a text representation of the object.
        return self.name



class Product(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unisex'),
    ]

    name = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    photo = models.ImageField(upload_to='products/', null=True, blank=True)
    
    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=7)

    def __str__(self):
        return self.name
    def get_color_code(self):
        return self.code


class ProductColor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} - {self.color.name}"

class BrandProduct(models.Model):
    # Relates the product to the brand, with cascade deletion and allows null values.
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    # Relates the brand to the product, with cascade deletion and allows null values.
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)

    # Represents the relationship in text with the IDs of the product and brand.
    def __str__(self):
        return f"Product ID {self.product.id} - Brand ID {self.brand.id}"



class CategoryProduct(models.Model):
    # Relates the product to the category, with cascade deletion and allows null values.
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    # Relates the category to the product, with cascade deletion and allows null values.
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    # Represents the relationship in text with the IDs of the product and category.
    def __str__(self):
        return f"Product ID {self.product.id} - Category ID {self.category.id}"



class Banner(models.Model):
    # Field to store the banner image
    photo = models.ImageField(upload_to='banners/')

    # Relationship with the brand using ForeignKey
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='banners', null=True)

    def __str__(self):
        return f"Banner of brand {self.brand.name}"
    

class BrandColor(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand.name} - {self.color.name}"