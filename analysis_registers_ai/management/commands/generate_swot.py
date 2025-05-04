# analysis_registers_ai/management/commands/generate_swot.py

import json
from django.core.management.base import BaseCommand
from recording_emotion.models import RecordingEmotion
from analysis_registers_ai.models import SWOTAnalysis
from analysis_registers_ai.utils import generate_swot_from_records

class Command(BaseCommand):
    help = 'Generar análisis DOFA por cada 30 registros emocionales'

    def handle(self, *args, **options):
        users = RecordingEmotion.objects.values_list('user', flat=True).distinct()
        for user_id in users:
            total_records = RecordingEmotion.objects.filter(user_id=user_id).count()
            last_analysis = SWOTAnalysis.objects.filter(user_id=user_id).order_by('-created_at').first()
            processed = last_analysis.processed_count if last_analysis else 0
            new_records = total_records - processed

            if new_records < 8:
                continue

            # Toma solo el slice de registros
            slice_start = processed
            slice_end = processed + 8
            records_qs = list(
                RecordingEmotion.objects.filter(user_id=user_id)
                .order_by('created_date')[slice_start:slice_end]
            )
            if not records_qs:
                continue

            period_start = records_qs[0].created_date.date()
            period_end = records_qs[-1].created_date.date()

            # Evita duplicados
            if SWOTAnalysis.objects.filter(user_id=user_id, period_start=period_start, period_end=period_end).exists():
                self.stdout.write(self.style.SUCCESS(
                    f"✔ Ya existe un análisis DOFA para el período {period_start} – {period_end}"
                ))
                continue

            # Prepara el texto
            entries_text = "\n".join(
                f"{r.created_date.date()}: {r.get_emotion_display()} - {r.description_day}"
                for r in records_qs
            )
            # Debug: muestra lo que envías
            self.stdout.write("🔍 Enviando a OpenAI (primeros 200 chars):")
            self.stdout.write(entries_text[:10] + ("…" if len(entries_text) > 10 else ""))

            # Llamada a la API en modo debug para ver la respuesta cruda
            raw = generate_swot_from_records(entries_text, debug=True)
            self.stdout.write("✅ Respuesta cruda de OpenAI:")
            self.stdout.write(raw)

            # Intentamos parsear el JSON
            try:
                data = json.loads(raw)
            except json.JSONDecodeError:
                self.stderr.write(self.style.ERROR(
                    "❌ No se pudo parsear la respuesta de OpenAI como JSON. "
                    "Revisa el contenido crudo mostrado arriba."
                ))
                continue

            # Crea el análisis con los datos parseados
            SWOTAnalysis.objects.create(
                user_id           = user_id,
                period_start      = period_start,
                period_end        = period_end,
                analysis          = data.get('analysis', ''),
                positive_patterns = data.get('positive_patterns', []),
                negative_patterns = data.get('negative_patterns', []),
                strengths         = data.get('strengths', ''),
                weaknesses        = data.get('weaknesses', ''),
                opportunities     = data.get('opportunities', ''),
                threats           = data.get('threats', ''),
                recommendations   = data.get('recommendations', ''),
                previous          = last_analysis,
                processed_count   = processed + 8
            )

            self.stdout.write(self.style.SUCCESS(
                f"✔ Generado DOFA para usuario {user_id} registros {processed + 1}–{processed + 8}"
            ))
            self.stdout.write(f"Total de registros del usuario {user_id}: {total_records}")
            self.stdout.write(f"Nuevos registros desde el último análisis: {new_records}")
