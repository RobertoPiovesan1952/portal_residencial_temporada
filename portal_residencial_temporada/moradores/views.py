from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Candidato, Morador, ContatoEmergencia
from .forms import MoradorForm

@login_required
def candidatos_lista(request):
    candidatos = Candidato.objects.all()
    return render(request, "candidatos/lista.html", {"candidatos": candidatos})

@login_required
def candidato_detalhe(request, pk):
    candidato = get_object_or_404(Candidato, pk=pk)
    return render(request, "candidatos/detalhe.html", {"candidato": candidato})

@login_required
def aprovar_candidato(request, pk):
    candidato = get_object_or_404(Candidato, pk=pk)
    if request.method == "POST":
        morador = Morador.objects.create(
            nome=candidato.nome,
            cpf=candidato.cpf,
            rg=candidato.rg,
            data_nascimento=candidato.data_nascimento,
            telefone=candidato.telefone,
            whatsapp=candidato.whatsapp,
            email=candidato.email,
            profissao=candidato.profissao,
            empresa=candidato.empresa,
            cidade_origem=candidato.cidade_origem,
        )
        ContatoEmergencia.objects.create(
            morador=morador,
            nome=candidato.emergencia_nome,
            parentesco=candidato.emergencia_parentesco,
            telefone=candidato.emergencia_telefone,
            whatsapp=candidato.emergencia_whatsapp,
            principal=True,
        )
        candidato.status = "convertido"
        candidato.save()
        messages.success(request, "Candidato aprovado e convertido em morador.")
        return redirect("morador_detalhe", pk=morador.pk)
    return render(request, "candidatos/aprovar.html", {"candidato": candidato})

@login_required
def moradores_lista(request):
    moradores = Morador.objects.all()
    return render(request, "moradores/lista.html", {"moradores": moradores})

@login_required
def morador_detalhe(request, pk):
    morador = get_object_or_404(Morador, pk=pk)
    if request.method == "POST":
        form = MoradorForm(request.POST, instance=morador)
        if form.is_valid():
            form.save()
            if morador.leito:
                morador.leito.status = "ocupado" if morador.status == "ativo" else "livre"
                morador.leito.save()
            messages.success(request, "Morador atualizado.")
            return redirect("morador_detalhe", pk=morador.pk)
    else:
        form = MoradorForm(instance=morador)
    return render(request, "moradores/detalhe.html", {"morador": morador, "form": form})
