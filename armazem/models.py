from django.db import models


"""
Aplicativos Django acessam e gerenciam dados através de objetos Python chamados de modelos (models).
Modelos definem a estrutura dos dados armazenados, incluindo os tipos de campos e possivelmente também o seu tamanho máximo,
valores default, opções de listas de seleção, texto de ajuda para documentação, texto de labels para formulários, etc.
"""

class Produto(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    catalogo = models.IntegerField()
    ultimo_update = models.DateTimeField(auto_now=True)

class Cliente(models.Model):
    ASSINATURA_BRONZE = 'B'
    ASSINATURA_PRATA = 'P'
    ASSINATURA_OURO = 'O'

    OPCOES_ASSINATURA = [
        (ASSINATURA_BRONZE, 'Bronze'),
        (ASSINATURA_PRATA, 'Prata'),
        (ASSINATURA_OURO, 'Ouro'),
    ]
    primeiro_nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    numero_contato = models.CharField(max_length=255)
    data_nascimento = models.DateField(null=True)
    assinatura = models.CharField(
        max_length=1, choices=OPCOES_ASSINATURA, default=ASSINATURA_BRONZE
    )

class Pedido(models.Model):
    STATUS_PAGAMENTO_PENDENTE = 'P'
    STATUS_PAGAMENTO_COMPLETO = 'C'
    STATUS_PAGAMENTO_FALHOU = 'F'
    
    OPCOES_PAGAMENTO = [
        (STATUS_PAGAMENTO_PENDENTE, 'Pending'),
        (STATUS_PAGAMENTO_COMPLETO, 'Completo'),
        (STATUS_PAGAMENTO_FALHOU, 'Falhou')        
    ]
    data_do_pedido = models.DateTimeField(auto_now_add=True)
    status_pagamento = models.CharField(
        max_length=1, choices=OPCOES_PAGAMENTO, default=STATUS_PAGAMENTO_PENDENTE
    )
