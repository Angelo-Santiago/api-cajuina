# orders/models.py

from django.db import models

class Table(models.Model):
    numero = models.IntegerField(unique=True)  # Número único para a mesa
    capacidade = models.IntegerField()  # Capacidade de pessoas

    def __str__(self):
        return f'Mesa {self.numero} - Capacidade: {self.capacidade}'

class Order(models.Model):
    # Campos para Order
    pass

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # outros campos

