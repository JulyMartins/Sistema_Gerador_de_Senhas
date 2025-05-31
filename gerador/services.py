from .models import Senha

class GerenciadorSenhas:
    especialidades = ["Clínico Geral", "Pediatria", "Ortopedia", "Ginecologia", "Dermatologia"]

    def gerar_codigo(self, tipo, especialidade, numero):
        return f"{tipo}{especialidade[0]}{str(numero).zfill(3)}"

    def gerar_senha(self, tipo, especialidade):
        contador = Senha.objects.count() + 1
        codigo = self.gerar_codigo(tipo, especialidade, contador)
        senha = Senha(tipo=tipo, especialidade=especialidade, codigo=codigo)
        senha.save()
        return senha

    def chamar_paciente_para_guiche(self, guiche_num):
        # Chama preferenciais que ainda não foram chamados
        preferenciais = Senha.objects.filter(tipo='P', chamado_para_guiche__isnull=True).order_by('id')
        if preferenciais.exists():
            senha = preferenciais.first()
            senha.chamado_para_guiche = guiche_num
            senha.save()
            return senha

        # Se não tem preferenciais, chama normais que ainda não foram chamados
        normais = Senha.objects.filter(tipo='N', chamado_para_guiche__isnull=True).order_by('id')
        if normais.exists():
            senha = normais.first()
            senha.chamado_para_guiche = guiche_num
            senha.save()
            return senha

        return None

    def fila_espera(self):
        return Senha.objects.filter(chamado_para_guiche__isnull=True).order_by('id')
