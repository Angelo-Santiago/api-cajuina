# forms.py
from django import forms
from .models import Category, Estoque, Item


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['nome', 'descricao']
        
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nome', 'descricao', 'preco', 'categoria']

class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['quantidade']

