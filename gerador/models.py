from django.db import models

class Senha(models.Model):
    TIPO_CHOICES = [
        ('N', 'Normal'),
        ('P', 'Preferencial'),
    ]

    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    especialidade = models.CharField(max_length=50)
    codigo = models.CharField(max_length=10, unique=True)
    chamado_para_guiche = models.IntegerField(null=True, blank=True)  # 1 ou 2 (guichê), ou None se não chamado ainda
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.codigo} - {self.get_tipo_display()} - {self.especialidade}"
