# reports/models.py

from django.db import models
from orders.models import Order, OrderItem
from django.utils import timezone

class Report(models.Model):
    nome = models.CharField(max_length=255)  # Nome do relatório (ex: "Relatório de Vendas de Janeiro")
    data_inicio = models.DateTimeField()  # Data de início do relatório
    data_fim = models.DateTimeField()  # Data de término do relatório
    total_vendas = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Total de vendas no período
    criado_em = models.DateTimeField(auto_now_add=True)  # Data de criação do relatório

    def gerar_relatorio(self):
        """
        Método para gerar o total de vendas no período do relatório.
        Ele calcula o total de vendas a partir dos pedidos dentro do intervalo de tempo.
        """
        total = 0
        # Obtém todos os pedidos no intervalo de tempo
        orders = Order.objects.filter(data__range=(self.data_inicio, self.data_fim), status='fechado')
        
        for order in orders:
            # Somando o total de cada pedido baseado nos itens
            total += sum(item.quantidade * item.preco_unitario for item in OrderItem.objects.filter(order=order))
        
        self.total_vendas = total
        self.save()

    def __str__(self):
        return f"{self.nome} - {self.data_inicio.strftime('%d/%m/%Y')} a {self.data_fim.strftime('%d/%m/%Y')}"
