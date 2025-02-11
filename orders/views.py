from django.shortcuts import render, redirect,get_object_or_404
from .forms import MesaForm
from .models import Table

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