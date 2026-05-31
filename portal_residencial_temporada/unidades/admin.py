from django.contrib import admin
from .models import Unidade, Quarto, Leito

class LeitoInline(admin.TabularInline):
    model = Leito
    extra = 0

class QuartoInline(admin.TabularInline):
    model = Quarto
    extra = 0

@admin.register(Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    list_display = ("nome", "cidade", "responsavel", "ativa")
    inlines = [QuartoInline]

@admin.register(Quarto)
class QuartoAdmin(admin.ModelAdmin):
    list_display = ("nome", "unidade", "capacidade", "ativo")
    inlines = [LeitoInline]

@admin.register(Leito)
class LeitoAdmin(admin.ModelAdmin):
    list_display = ("codigo", "quarto", "status", "valor_sugerido")
    list_filter = ("status", "quarto")
