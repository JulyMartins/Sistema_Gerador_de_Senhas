from django.shortcuts import render, redirect
from .services import GerenciadorSenhas

gerenciador = GerenciadorSenhas()

def index(request):
    mensagem = None
    if request.method == 'POST':
        tipo = request.POST.get('preferencial')
        especialidade = request.POST.get('setor')

        if tipo == '1':
            tipo = 'P'
        else:
            tipo = 'N'

        if especialidade not in gerenciador.especialidades:
            mensagem = "Especialidade inválida."
        else:
            senha = gerenciador.gerar_senha(tipo, especialidade)
            mensagem = f"Senha gerada: {senha.codigo} para {senha.especialidade}"

    context = {
        'mensagem': mensagem,
        'consultorios': gerenciador.especialidades,
    }
    return render(request, 'gerador/gerar_senha.html', context)

def painel(request):
    guiche1 = gerenciador.chamar_paciente_para_guiche(1)
    guiche2 = gerenciador.chamar_paciente_para_guiche(2)

    fila_espera = gerenciador.fila_espera()

    context = {
        'guiche1': guiche1,
        'guiche2': guiche2,
        'fila_espera': fila_espera,
    }
    return render(request, 'gerador/painel.html', context)

def resetar(request):
    from .models import Senha
    Senha.objects.all().delete()
    return redirect('index')
