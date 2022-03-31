"""
Neste módulo é onde fica o mapeamento da url para a views
"""

from django.urls import path
from . import views


# Configuração da URL
urlpatterns = [
    path('ola/', views.diga_ola)
]
