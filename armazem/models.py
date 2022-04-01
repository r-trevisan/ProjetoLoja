from django.db import models


"""
Aplicativos Django acessam e gerenciam dados através de objetos Python chamados de modelos (models).
Modelos definem a estrutura dos dados armazenados, incluindo os tipos de campos e possivelmente também o seu tamanho máximo,
valores default, opções de listas de seleção, texto de ajuda para documentação, texto de labels para formulários, etc.

Foram inseridas relações OneToOne, OneToMany e ManyToMany.
"""

class Promocao(models.Model):
    descricao = models.CharField(max_length=255)
    desconto = models.FloatField()


class Acervo(models.Model):
    titulo = models.CharField(max_length=255)


class Produto(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    catalogo = models.IntegerField()
    ultimo_update = models.DateTimeField(auto_now=True)
    acervo = models.ForeignKey(Acervo, on_delete=models.PROTECT) # protege os produtos de um acervo caso você o delete
    promocoes = models.ManyToManyField(Promocao)


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
        max_length=1, choices=OPCOES_PAGAMENTO, default=STATUS_PAGAMENTO_PENDENTE)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT) # protege os pedidos caso a classe Cliente seja deletada


class Produtos_Pedidos(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveSmallIntegerField() #protege contra números negativos
    preco_unitario = models.DecimalField(max_digits=6, decimal_places=2)


# Caso a Classe Cliente seja deletada, o atributo cliente também será deletado
class Endereco(models.Model):
    rua = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE) #podem ser inseridos vários endereços para o mesmo cliente


class Carrinho(models.Model):
    data_de_criacao = models.DateTimeField(auto_now_add=True)


class Itens_carrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveSmallIntegerField()
