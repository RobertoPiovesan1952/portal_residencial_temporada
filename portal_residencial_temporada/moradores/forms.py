from django import forms
from .models import Candidato, Morador

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = [
            "nome", "cpf", "rg", "data_nascimento", "telefone", "whatsapp", "email",
            "profissao", "empresa", "cidade_origem",
            "emergencia_nome", "emergencia_parentesco", "emergencia_telefone", "emergencia_whatsapp",
            "documento_rg_cnh", "comprovante_residencia", "foto_pessoal",
            "fuma", "aceita_regras", "observacoes",
        ]
        widgets = {
            "data_nascimento": forms.DateInput(attrs={"type": "date"}),
            "observacoes": forms.Textarea(attrs={"rows": 3}),
            "aceita_regras": forms.CheckboxInput(),
        }

class MoradorForm(forms.ModelForm):
    class Meta:
        model = Morador
        fields = [
            "nome", "cpf", "rg", "data_nascimento", "telefone", "whatsapp", "email",
            "profissao", "empresa", "cidade_origem",
            "unidade", "quarto", "leito", "valor_contratado", "data_entrada", "status",
            "chave_entregue", "controle_portao_entregue", "wifi_entregue",
        ]
        widgets = {
            "data_nascimento": forms.DateInput(attrs={"type": "date"}),
            "data_entrada": forms.DateInput(attrs={"type": "date"}),
        }
