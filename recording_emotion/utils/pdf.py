# recording_emotion/utils/pdf.py

import io
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from django.utils import timezone

# (mapa de MESES si lo tienes)
MESES = {
    1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril',
    5: 'mayo', 6: 'junio', 7: 'julio', 8: 'agosto',
    9: 'septiembre', 10: 'octubre', 11: 'noviembre', 12: 'diciembre',
}

def generate_registros_pdf(registros):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        leftMargin=inch, rightMargin=inch,
        topMargin=inch, bottomMargin=inch,
    )

    styles = getSampleStyleSheet()
    normal = styles['Normal']
    normal.leading = 14

    story = []
    for registro in registros.order_by('created_date'):
        # <-- convertimos a la zona local de Bogotá
        fecha_utc = registro.created_date
        fecha_local = timezone.localtime(fecha_utc)

        dia  = fecha_local.day
        mes  = MESES[fecha_local.month]
        anio = fecha_local.year
        fecha_str = f"{dia} de {mes} {anio}"

        # Construyo un párrafo con HTML básico: fecha en negrita + descripción
        texto = (
            f"<b>Registro: {fecha_str} — {registro.get_emotion_display()}</b><br/>"
            f"{registro.description_day.replace('\n', '<br/>')}"
        )
        p = Paragraph(texto, normal)
        story.append(p)
        story.append(Spacer(1, 0.2 * inch))

    doc.build(story)
    buffer.seek(0)
    return buffer

