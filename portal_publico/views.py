from django.shortcuts import render, redirect
from django.contrib import messages
from moradores.forms import CandidatoForm
from unidades.models import Quarto, Leito

def home(request):
    vagas_livres = Leito.objects.filter(status="livre").count()
    return render(request, "publico/home.html", {"vagas_livres": vagas_livres})

def estrutura(request):
    return render(request, "publico/estrutura.html")

def regras(request):
    return render(request, "publico/regras.html")

def solicitar_vaga(request):
    if request.method == "POST":
        form = CandidatoForm(request.POST, request.FILES)
        if form.is_valid():
            candidato = form.save(commit=False)
            candidato.status = "novo"
            candidato.save()
            messages.success(request, "Sua solicitação foi enviada com sucesso.")
            return redirect("obrigado")
    else:
        form = CandidatoForm()
    return render(request, "publico/solicitar_vaga.html", {"form": form})

def obrigado(request):
    return render(request, "publico/obrigado.html")
