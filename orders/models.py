from django.db import models

class Table(models.Model):
    number = models.IntegerField(unique=True)  # Número único para a mesa
    capacity = models.IntegerField()  # Capacidade de pessoas

    def __str__(self):
        return f'Mesa {self.number} - Capacidade: {self.capacity}'

class Order(models.Model):
    PENDING = 'P'
    COMPLETED = 'C'
    CANCELLED = 'X'
    
    STATUS_CHOICES = [
        (PENDING, 'Pendente'),
        (COMPLETED, 'Concluído'),
        (CANCELLED, 'Cancelado'),
    ]
    
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)  # Mesa associada ao pedido, mas é opcional
    customer_name = models.CharField(max_length=100)  # Nome do cliente
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Preço total do pedido
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default=PENDING
    )  # Status do pedido
    created_at = models.DateTimeField(auto_now_add=True)  # Data e hora de criação
    updated_at = models.DateTimeField(auto_now=True)  # Data e hora da última atualização

    def __str__(self):
        return f'Pedido #{self.id} - {self.customer_name} - Status: {self.get_status_display()}'

    def update_total_price(self):
        """Atualiza o preço total com base nos itens do pedido."""
        total = sum(item.total_price() for item in self.orderitem_set.all())
        self.total_price = total
        self.save()

    def add_item(self, product_name, quantity, price):
        """Adiciona um item ao carrinho (cria um OrderItem e atualiza o total)."""
        item = OrderItem.objects.create(
            order=self,
            product_name=product_name,
            quantity=quantity,
            price=price
        )
        self.update_total_price()
        return item

    def remove_item(self, item_id):
        """Remove um item do carrinho e atualiza o total."""
        item = self.orderitem_set.get(id=item_id)
        item.delete()
        self.update_total_price()

    def checkout(self):
        """Finaliza o pedido (envio do pedido e alteração de status)."""
        self.status = self.COMPLETED
        self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  # Relaciona o item ao pedido
    product_name = models.CharField(max_length=200)  # Nome do produto
    quantity = models.IntegerField()  # Quantidade do produto
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Preço do produto

    def total_price(self):
        """Calcula o preço total do item (quantidade * preço)."""
        return self.quantity * self.price

    def __str__(self):
        return f'{self.product_name} - {self.quantity} x {self.price}'