from django.urls import path
from . import views

urlpatterns = [
    path('mesas/', views.listar_mesas, name='listar_mesas'),
    path('mesas/criar/', views.criar_mesa, name='criar_mesa'),
    path('mesas/<int:pk>/atualizar/', views.atualizar_mesa, name='atualizar_mesa'),
    path('mesas/<int:pk>/deletar/', views.deletar_mesa, name='deletar_mesa'),
]
