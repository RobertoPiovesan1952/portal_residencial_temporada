# Portal Residencial Temporada

Primeira versão funcional do sistema para gestão de moradia compartilhada masculina.

## O que já vem pronto

- Site público
- Formulário de solicitação de vaga
- Upload de documentos do candidato
- Login administrativo
- Dashboard
- Cadastro de unidade, quartos e vagas
- Candidatos
- Conversão de candidato em morador
- Contato de emergência
- Cadastro de moradores
- Financeiro inicial via admin Django
- Contratos iniciais via admin Django

## Como rodar localmente

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_residencial
python manage.py runserver
```

Acesse:

- Site: http://127.0.0.1:8000/
- Portal: http://127.0.0.1:8000/portal/
- Admin Django: http://127.0.0.1:8000/admin/

## Próximos módulos

- Contrato PDF automático
- Assinatura digital
- Pagamentos
- WhatsApp
- Portal do morador
