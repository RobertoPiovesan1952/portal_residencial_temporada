from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Sum
from unidades.models import Leito, Quarto
from moradores.models import Candidato, Morador, Contrato
from financeiro.models import Pagamento

@login_required
def dashboard(request):
    total_vagas = Leito.objects.count()
    vagas_ocupadas = Leito.objects.filter(status="ocupado").count()
    vagas_livres = Leito.objects.filter(status="livre").count()
    moradores_ativos = Morador.objects.filter(status="ativo").count()
    candidatos_novos = Candidato.objects.filter(status="novo").count()
    receita_prevista = Morador.objects.filter(status="ativo").aggregate(total=Sum("valor_contratado"))["total"] or 0
    pagamentos_abertos = Pagamento.objects.filter(status__in=["aberto", "atrasado"]).aggregate(total=Sum("valor"))["total"] or 0
    quartos = Quarto.objects.prefetch_related("leitos").all()

    return render(request, "admin_portal/dashboard.html", {
        "total_vagas": total_vagas,
        "vagas_ocupadas": vagas_ocupadas,
        "vagas_livres": vagas_livres,
        "moradores_ativos": moradores_ativos,
        "candidatos_novos": candidatos_novos,
        "receita_prevista": receita_prevista,
        "pagamentos_abertos": pagamentos_abertos,
        "quartos": quartos,
    })
