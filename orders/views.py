from django.shortcuts import render, redirect,get_object_or_404
from .forms import MesaForm
from .models import Table,Order,OrderItem
from django.http import JsonResponse

def criar_mesa(request):
    if request.method == 'POST':
        form = MesaForm(request.POST)  # Passando os dados do formulário
        if form.is_valid():  # Verificando se os dados são válidos
            form.save()  # Salvando a mesa no banco
            return redirect('listar_mesas')  # Redireciona para a lista de mesas após salvar
    else:
        form = MesaForm()  # Se não for um POST, apenas exibe o formulário vazio

    return render(request, 'criar_mesa.html', {'form': form})


def atualizar_mesa(request, pk):
    mesa = get_object_or_404(Table, pk=pk)  # Busca a mesa pelo ID
    if request.method == 'POST':
        form = MesaForm(request.POST, instance=mesa)  # Passa os dados da mesa existente
        if form.is_valid():
            form.save()  # Atualiza a mesa no banco de dados
            return redirect('listar_mesas')  # Redireciona para a lista de mesas
    else:
        form = MesaForm(instance=mesa)  # Exibe o formulário com os dados da mesa

    return render(request, 'atualizar_mesa.html', {'form': form})

def deletar_mesa(request, pk):
    mesa = get_object_or_404(Table, pk=pk)
    mesa.delete()
    return redirect('listar_mesas')  # Redireciona após deletar

#carrinho

def add_item_to_cart(request):
    customer_name = request.POST['customer_name']
    product_name = request.POST['product_name']
    quantity = int(request.POST['quantity'])
    price = float(request.POST['price'])
    table_id = request.POST.get('table_id', None)  # Pode ser None se o pedido for sem mesa
    
    # Se o pedido for associado a uma mesa, buscamos a mesa pelo ID
    table = None
    if table_id:
        table = get_object_or_404(Table, id=table_id)
    
    # Criar ou obter o pedido (caso já tenha um pedido existente)
    order, created = Order.objects.get_or_create(
        customer_name=customer_name, 
        table=table,  # A mesa será associada se for fornecida
        status=Order.PENDING
    )
    
    # Adicionar item ao pedido (carrinho)
    order.add_item(product_name, quantity, price)
    
    return JsonResponse({"message": "Item adicionado ao carrinho", "total": order.total_price})

def remove_item_from_cart(request, item_id):
    # Buscar o item que será removido
    item = get_object_or_404(OrderItem, id=item_id)
    
    # Obter o pedido ao qual o item pertence
    order = item.order
    
    # Remover o item do pedido e atualizar o preço
    order.remove_item(item_id)
    
    return JsonResponse({"message": "Item removido do carrinho", "total": order.total_price})

def checkout_order(request):
    customer_name = request.POST['customer_name']
    
    # Obter o pedido do cliente
    order = get_object_or_404(Order, customer_name=customer_name, status=Order.PENDING)
    
    # Finalizar o pedido (marcar como concluído)
    order.checkout()
    
    return JsonResponse({"message": "Pedido finalizado", "total": order.total_price})