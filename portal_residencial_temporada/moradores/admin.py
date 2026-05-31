from django.contrib import admin
from .models import Candidato, Morador, ContatoEmergencia, Contrato, Ocorrencia

class ContatoEmergenciaInline(admin.TabularInline):
    model = ContatoEmergencia
    extra = 0

class ContratoInline(admin.TabularInline):
    model = Contrato
    extra = 0

@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ("nome", "telefone", "empresa", "cidade_origem", "status", "criado_em")
    list_filter = ("status", "fuma", "aceita_regras")
    search_fields = ("nome", "cpf", "telefone", "empresa")

@admin.register(Morador)
class MoradorAdmin(admin.ModelAdmin):
    list_display = ("nome", "quarto", "leito", "valor_contratado", "status")
    list_filter = ("status", "quarto")
    search_fields = ("nome", "cpf", "telefone", "empresa")
    inlines = [ContatoEmergenciaInline, ContratoInline]

@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ("tipo", "morador", "criada_em", "resolvida")
    list_filter = ("tipo", "resolvida")
