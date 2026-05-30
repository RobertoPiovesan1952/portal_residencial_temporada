from django.core.management.base import BaseCommand
from unidades.models import Unidade, Quarto, Leito

class Command(BaseCommand):
    help = "Cria a unidade inicial, 5 quartos e 10 vagas."

    def handle(self, *args, **options):
        unidade, _ = Unidade.objects.get_or_create(
            nome="Residencial Temporada",
            defaults={
                "cidade": "",
                "responsavel": "",
                "telefone": "",
            }
        )

        for i in range(1, 6):
            quarto, _ = Quarto.objects.get_or_create(
                unidade=unidade,
                nome=f"Quarto {i}",
                defaults={"capacidade": 2}
            )
            for codigo in ["A", "B"]:
                Leito.objects.get_or_create(
                    quarto=quarto,
                    codigo=codigo,
                    defaults={"status": "livre", "valor_sugerido": 750}
                )

        self.stdout.write(self.style.SUCCESS("Residencial inicial criado com 5 quartos e 10 vagas."))
