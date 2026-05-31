from django.db import models

class Unidade(models.Model):
    nome = models.CharField(max_length=120, default="Residencial Temporada")
    endereco = models.CharField(max_length=255, blank=True)
    cidade = models.CharField(max_length=120, blank=True)
    telefone = models.CharField(max_length=30, blank=True)
    responsavel = models.CharField(max_length=120, blank=True)
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Quarto(models.Model):
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, related_name="quartos")
    nome = models.CharField(max_length=80)
    capacidade = models.PositiveIntegerField(default=2)
    observacoes = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} - {self.unidade.nome}"

    @property
    def ocupacao_atual(self):
        return self.leitos.filter(status="ocupado").count()

class Leito(models.Model):
    STATUS_CHOICES = [
        ("livre", "Livre"),
        ("reservado", "Reservado"),
        ("ocupado", "Ocupado"),
        ("manutencao", "Manutenção"),
    ]

    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE, related_name="leitos")
    codigo = models.CharField(max_length=30)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="livre")
    valor_sugerido = models.DecimalField(max_digits=10, decimal_places=2, default=750)
    observacoes = models.TextField(blank=True)

    class Meta:
        ordering = ["quarto__nome", "codigo"]
        unique_together = ["quarto", "codigo"]

    def __str__(self):
        return f"{self.quarto.nome} - {self.codigo}"
