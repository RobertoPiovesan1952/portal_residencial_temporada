from django.db import models
from moradores.models import Morador, Contrato

class Pagamento(models.Model):
    STATUS_CHOICES = [
        ("aberto", "Aberto"),
        ("pago", "Pago"),
        ("atrasado", "Atrasado"),
        ("cancelado", "Cancelado"),
    ]

    FORMA_CHOICES = [
        ("pix", "PIX"),
        ("transferencia", "Transferência"),
        ("dinheiro", "Dinheiro"),
        ("cartao", "Cartão"),
        ("outro", "Outro"),
    ]

    morador = models.ForeignKey(Morador, on_delete=models.CASCADE, related_name="pagamentos")
    contrato = models.ForeignKey(Contrato, on_delete=models.SET_NULL, null=True, blank=True, related_name="pagamentos")
    competencia = models.CharField(max_length=7, help_text="Exemplo: 2026-06")
    vencimento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField(null=True, blank=True)
    forma_pagamento = models.CharField(max_length=20, choices=FORMA_CHOICES, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="aberto")
    observacoes = models.TextField(blank=True)

    class Meta:
        ordering = ["vencimento"]
