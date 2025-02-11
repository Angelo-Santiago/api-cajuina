from django.shortcuts import render, redirect
from .models import Mesa
from .forms import MesaForm  # Supondo que você tenha um formulário de Mesa

def criar_mesa(request):
    if request.method == 'POST':
        form = MesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_mesas')  # Redireciona para a página de listagem
    else:
        form = MesaForm()
    return render(request, 'criar_mesa.html', {'form': form})
