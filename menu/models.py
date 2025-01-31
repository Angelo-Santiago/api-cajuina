# menu/models.py

from django.db import models

# Categoria do Menu
class Category(models.Model):
    nome = models.CharField(max_length=255)  # Nome da categoria (ex: "Bebidas", "Pratos principais")
    descricao = models.TextField()  # Descrição da categoria (opcional)

    def __str__(self):
        return self.nome


# Item do Menu
class Item(models.Model):
    nome = models.CharField(max_length=255)  # Nome do item (ex: "Coca-Cola", "Pizza Margherita")
    descricao = models.TextField()  # Descrição do item (opcional)
    preco = models.DecimalField(max_digits=10, decimal_places=2)  # Preço do item
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE)  # Categoria a qual o item pertence

    def __str__(self):
        return self.nome


# Estoque do Item
class Estoque(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)  # Relacionamento 1:1 com o item
    quantidade = models.IntegerField()  # Quantidade em estoque do item

    def __str__(self):
        return f"Estoque de {self.item.nome}: {self.quantidade} unidades"
