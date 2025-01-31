# orders/models.py

from django.db import models

class Table(models.Model):
    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('ocupada', 'Ocupada'),
    ]
    
    numero = models.IntegerField(unique=True)  # Número da mesa
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='disponivel')  # Status da mesa
    
    def __str__(self):
        return f"Mesa {self.numero} - Status: {self.status}"


class Order(models.Model):
    STATUS_CHOICES = [
        ('aberto', 'Aberto'),
        ('fechado', 'Fechado'),
    ]
    
    numero = models.IntegerField(unique=True)  # Número do pedido
    data = models.DateTimeField(auto_now_add=True)  # Data do pedido
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='aberto')  # Status do pedido
    mesa = models.ForeignKey(Table, null=True, blank=True, on_delete=models.SET_NULL)  # Mesa associada (opcional)

    def __str__(self):
        return f"Pedido {self.numero} - Status: {self.status} - Mesa: {self.mesa.numero if self.mesa else 'Sem mesa'}"

