from django.contrib import admin
from .models import Pagamento

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ("morador", "competencia", "vencimento", "valor", "status", "data_pagamento")
    list_filter = ("status", "forma_pagamento")
    search_fields = ("morador__nome", "competencia")
