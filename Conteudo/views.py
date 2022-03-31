from django.shortcuts import render
from django.http import HttpResponse

'''
Aqui é onde são definidas as Views
Views é uma função que solicita (request) algo e recebe uma resposta (response). 
É uma request handler. Arquitetamente falando ela está associada com algo 
que o usuário vê.
'''

def diga_ola(request):
    # aqui podemos pegar/transformar dados de um database, enviar emails, etc...
    return render(request, 'ola.html', { 'name': 'Rafa'})

'''
após definida a função devemos mapear até a URL, para que quando a URL receber
um request essa função aqui será a resposta(será chamada).
'''
