# urls.py
from django.urls import path
from . import views

urlpatterns = [
    #category
    path('', views.list_categories, name='list_categories'),
    path('category/new/', views.create_category, name='create_category'),
    path('category/<int:pk>/edit/', views.edit_category, name='edit_category'),
    path('category/<int:pk>/delete/', views.delete_category, name='delete_category'),
    #estoque
    path('estoques/', views.estoque_list, name='estoque_list'),
    path('estoque/<int:item_id>/update/', views.update_estoque, name='update_estoque'),
    path('estoque/<int:item_id>/delete/', views.delete_estoque, name='delete_estoque'),
    #item
    path('items/', views.item_list, name='item_list'),  # Lista de itens
    path('item/new/', views.create_item, name='create_item'),  # Criar item
    path('item/<int:pk>/edit/', views.edit_item, name='edit_item'),  # Editar item
    path('item/<int:pk>/delete/', views.delete_item, name='delete_item'),  # Excluir item
]
