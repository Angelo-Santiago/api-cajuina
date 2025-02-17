from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategoryForm, EstoqueForm, ItemForm
from .models import Category, Estoque, Item

#Category
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_categories')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})


def list_categories(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})


def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('list_categories')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('list_categories')
    return render(request, 'category_confirm_delete.html', {'category': category})


#item

def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'item_form.html', {'form': form})

def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'item_form.html', {'form': form})

def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'item_confirm_delete.html', {'item': item})

#Estoque
def update_estoque(request, item_id):
    item = get_object_or_404(Item, id=item_id)  # Obtém o item pelo ID
    estoque, created = Estoque.objects.get_or_create(item=item)  # Se já existe estoque para o item, pega ou cria

    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance=estoque)
        if form.is_valid():
            form.save()
            return redirect('estoque_list')
    else:
        form = EstoqueForm(instance=estoque)

    return render(request, 'estoque_form.html', {'form': form, 'item': item})

# Listar todos os itens e seus estoques
def estoque_list(request):
    estoques = Estoque.objects.all()
    return render(request, 'estoque_list.html', {'estoques': estoques})


def delete_estoque(request, item_id):
    estoque = get_object_or_404(Estoque, item__id=item_id)
    if request.method == 'POST':
        estoque.delete()
        return redirect('estoque_list')
    return render(request, 'estoque_confirm_delete.html', {'estoque': estoque})

