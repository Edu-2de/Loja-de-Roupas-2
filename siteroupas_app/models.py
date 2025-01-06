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

      # define o nome do produto
      nome = models.CharField(max_length=50)

      # define a marca do produto, se adequando as marcas pedentes na tabela marcas
      marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

      # define o preco do produto
      preco = models.CharField(max_length=20)

      # define a cetgoria do produto, como calcado, camiseta...
      categoria = models.CharField(max_length=20)

      # define o genro para qual o produto foi feito
      genero = models.CharField(max_length=5, null=True)

      # Define uma relação muitos-para-muitos entre `Produto` e `Marca`.
      # Especifica o modelo intermediário `MarcaProduto`.
      marcas = models.ManyToManyField(
            Marca, 
            through='MarcaProduto', 
            related_name='produtos'
      )

      categorias = models.ManyToManyField(
            Categoria, 
            through='CategoriaProduto', 
            related_name='produtos'
      )


      def __str__(self):
            # Retorna o nome completo do produto como representação em texto do objeto.
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



