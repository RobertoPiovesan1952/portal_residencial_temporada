from django.db import models
from django.utils import timezone
from unidades.models import Unidade, Quarto, Leito

class Candidato(models.Model):
    STATUS_CHOICES = [
        ("novo", "Novo"),
        ("analise", "Em análise"),
        ("aprovado", "Aprovado"),
        ("reprovado", "Reprovado"),
        ("espera", "Lista de espera"),
        ("convertido", "Convertido em morador"),
    ]

    nome = models.CharField(max_length=160)
    cpf = models.CharField(max_length=20, blank=True)
    rg = models.CharField(max_length=30, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    telefone = models.CharField(max_length=30)
    whatsapp = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    profissao = models.CharField(max_length=120, blank=True)
    empresa = models.CharField(max_length=160, blank=True)
    cidade_origem = models.CharField(max_length=120, blank=True)

    emergencia_nome = models.CharField(max_length=160)
    emergencia_parentesco = models.CharField(max_length=80)
    emergencia_telefone = models.CharField(max_length=30)
    emergencia_whatsapp = models.CharField(max_length=30, blank=True)

    documento_rg_cnh = models.FileField(upload_to="documentos/candidatos/", blank=True, null=True)
    comprovante_residencia = models.FileField(upload_to="documentos/candidatos/", blank=True, null=True)
    foto_pessoal = models.FileField(upload_to="documentos/candidatos/", blank=True, null=True)

    fuma = models.BooleanField(default=False)
    aceita_regras = models.BooleanField(default=False)
    observacoes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="novo")
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-criado_em"]

    def __str__(self):
        return self.nome

class Morador(models.Model):
    STATUS_CHOICES = [
        ("ativo", "Ativo"),
        ("encerrado", "Encerrado"),
        ("inadimplente", "Inadimplente"),
        ("renovacao", "Em renovação"),
    ]

    nome = models.CharField(max_length=160)
    cpf = models.CharField(max_length=20, blank=True)
    rg = models.CharField(max_length=30, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    telefone = models.CharField(max_length=30)
    whatsapp = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    profissao = models.CharField(max_length=120, blank=True)
    empresa = models.CharField(max_length=160, blank=True)
    cidade_origem = models.CharField(max_length=120, blank=True)

    unidade = models.ForeignKey(Unidade, on_delete=models.SET_NULL, null=True, blank=True)
    quarto = models.ForeignKey(Quarto, on_delete=models.SET_NULL, null=True, blank=True)
    leito = models.ForeignKey(Leito, on_delete=models.SET_NULL, null=True, blank=True)

    valor_contratado = models.DecimalField(max_digits=10, decimal_places=2, default=750)
    data_entrada = models.DateField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="ativo")

    chave_entregue = models.BooleanField(default=False)
    controle_portao_entregue = models.BooleanField(default=False)
    wifi_entregue = models.BooleanField(default=False)

    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome

class ContatoEmergencia(models.Model):
    morador = models.ForeignKey(Morador, on_delete=models.CASCADE, related_name="contatos_emergencia")
    nome = models.CharField(max_length=160)
    parentesco = models.CharField(max_length=80)
    telefone = models.CharField(max_length=30)
    whatsapp = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    principal = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} ({self.parentesco})"

class Contrato(models.Model):
    STATUS_CHOICES = [
        ("aguardando", "Aguardando assinatura"),
        ("ativo", "Ativo"),
        ("renovado", "Renovado"),
        ("encerrado", "Encerrado"),
    ]

    morador = models.ForeignKey(Morador, on_delete=models.CASCADE, related_name="contratos")
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor_mensal = models.DecimalField(max_digits=10, decimal_places=2)
    renovacao_automatica = models.BooleanField(default=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="aguardando")
    arquivo_pdf = models.FileField(upload_to="contratos/", blank=True, null=True)
    assinado = models.BooleanField(default=False)

    def __str__(self):
        return f"Contrato - {self.morador.nome}"

class Ocorrencia(models.Model):
    TIPO_CHOICES = [
        ("advertencia", "Advertência"),
        ("manutencao", "Manutenção"),
        ("reclamacao", "Reclamação"),
        ("observacao", "Observação"),
    ]

    morador = models.ForeignKey(Morador, on_delete=models.SET_NULL, null=True, blank=True, related_name="ocorrencias")
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descricao = models.TextField()
    responsavel = models.CharField(max_length=120, blank=True)
    criada_em = models.DateTimeField(auto_now_add=True)
    resolvida = models.BooleanField(default=False)

    class Meta:
        ordering = ["-criada_em"]
