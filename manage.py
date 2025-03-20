#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


from orders.order import processar_order

# Exemplo de order (pedido)
order = {
    'id': 124,
    'produto': 'Pizza Margherita',
    'quantidade': 1,
    'preco': 25.00,
    'observacoes': 'Sem queijo extra'
}

# Defina se deve usar a impressora térmica ou gerar o PDF
usar_impressora_termica = True  # Mude para False para gerar o PDF

# Processa o pedido (order)
processar_order(order, usar_impressora_termica)
