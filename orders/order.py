# orders/order.py

from orders.printing import imprimir_ticket, gerar_pdf

# Função para processar um novo pedido
def processar_order(order, usar_impressora_termica=True):
    if usar_impressora_termica:
        imprimir_ticket(order)  # Imprime na impressora térmica
    else:
        gerar_pdf(order)  # Gera PDF e salva no disco
