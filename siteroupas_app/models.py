from django.db import models

# Create your models here.

class Marca(models.Model):

      # Campo para armazenar o nome completo da marca.
      nome = models.CharField(max_length=50)

      # armazena a cor principal da marca
      cor = models.CharField(max_length=10)

      # Novo campo para a logo
      logo = models.ImageField(upload_to='marcas_logos/', null=True, blank=True)


      def __str__(self):
            # Retorna o nome completo da marca como representação em texto do objeto.
            return self.nome





class Categoria(models.Model):

      # Campo para armazenar o nome completo da marca.
      nome = models.CharField(max_length=50)

      def __str__(self):
            # Retorna o nome completo da categoria como representação em texto do objeto.
            return self.nome





class Produto(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('U', 'Unissex'),
    ]

    nome = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    preco = models.CharField(max_length=20)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    cor = models.CharField(max_length=10, null=True, blank=True)
    foto = models.ImageField(upload_to='produtos/', null=True, blank=True)
    
    def __str__(self):
        return self.nome

  



class MarcaProduto(models.Model):

      # Relaciona o produto á marca, com remoção em cascata e permite valor nulo.
      produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True)

      # Relaciona a marca ao produto, com remoção em cascata e permite valor nulo.
      marca = models.ForeignKey(Marca, on_delete=models.CASCADE, null=True)

      # Representa a relação em texto com os IDs do produto e da marca.
      def __str__(self):
            return f"Produto ID {self.produto.id} - Marca ID {self.marca.id}"





class CategoriaProduto(models.Model):

      # Relaciona o produto á marca, com remoção em cascata e permite valor nulo.
      produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True)

      # Relaciona a categoria ao produto, com remoção em cascata e permite valor nulo.
      Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)

      # Representa a relação em texto com os IDs do produto e da categoria.
      def __str__(self):
            return f"Produto ID {self.produto.id} - Marca ID {self.Categoria.id}"




class Banner(models.Model):
      # Campo para armazenar a imagem do banner
      foto = models.ImageField(upload_to='banners/')
      
      # Relacionamento com a marca usando ForeignKey
      marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='banners')

      def __str__(self):
            return f"Banner da marca {self.marca.nome}"



