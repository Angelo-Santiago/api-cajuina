

from django.contrib import admin
from .models import Table

# Admin para o modelo Table
class TableAdmin(admin.ModelAdmin):
    list_display = ['number', 'capacity']  # Exibe as colunas 'numero' e 'capacidade'
    search_fields = ['number']  # Permite pesquisa pelo número da mesa
    list_filter = ['capacity']  # Filtra mesas pela capacidade
    ordering = ['number']  # Ordena as mesas pelo número
    list_per_page = 10  # Exibe 10 itens por página na listagem

# Registra o modelo Table no Django Admin com a configuração personalizada
admin.site.register(Table, TableAdmin)
