from django.urls import path
from .views import index, painel, resetar

urlpatterns = [
    path('', index, name='index'),             # Página para gerar senha
    path('painel/', painel, name='painel'),    # Painel de atendimento
    path('resetar/', resetar, name='resetar'), # Reseta as senhas
]



