from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_mesas, name='lista_mesas'),
    path('mesas/criar/', views.criar_mesa, name='criar_mesa'),
    path('mesas/<int:pk>/atualizar/', views.atualizar_mesa, name='atualizar_mesa'),
    path('mesas/<int:pk>/deletar/', views.deletar_mesa, name='deletar_mesa'),
    path('mesa/<int:mesa_id>/', views.ver_mesa, name='ver_mesa'),
    path('gerar_qrcode/<int:mesa_id>/', views.gerar_qrcode, name='gerar_qrcode'),
    

]
