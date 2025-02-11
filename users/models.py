# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    TIPO_CHOICES = [
        ('atendente', 'Atendente'),
        ('admin', 'Admin'),
        ('gerente', 'Gerente'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='atendente')  # Tipo de usuário
    data_nascimento = models.DateField(null=True, blank=True)  # Data de nascimento (opcional)
    telefone = models.CharField(max_length=15, null=True, blank=True)  # Telefone (opcional)
    
     # Define o related_name para evitar o conflito
    groups = models.ManyToManyField(
        'auth.Group', related_name='user_set_users', blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='user_set_users', blank=True
    )

    def __str__(self):
        return self.username
