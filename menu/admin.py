from django.contrib import admin
from .models import Category, Item

# Registra o modelo Category no Django Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao']  # Exibe essas colunas na lista
    search_fields = ['nome']  # Permite pesquisar por nome da categoria

admin.site.register(Category, CategoryAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'categoria', 'descricao']  # Exibe essas colunas na lista
    search_fields = ['nome', 'descricao']  # Permite pesquisar por nome ou descrição
    list_filter = ['categoria']  # Filtra por categoria
    ordering = ['nome']  # Ordena por nome
    list_per_page = 10  # Limita o número de itens exibidos por página no admin

admin.site.register(Item, ItemAdmin)