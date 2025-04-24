# recording_emotion/utils/pdf.py

import io
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

def generate_registros_pdf(registros):
    """
    Genera un PDF con márgenes de 1 inch en todos los lados,
    ajusta texto automáticamente y coloca un pequeño espacio entre entradas.
    """
    buffer = io.BytesIO()

    # Creamos el documento, tamaño carta y 1" de margen
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        leftMargin=inch,
        rightMargin=inch,
        topMargin=inch,
        bottomMargin=inch,
    )

    # Obtengo estilos de párrafo predefinidos
    styles = getSampleStyleSheet()
    normal = styles['Normal']
    normal.leading = 14  # altura de línea en puntos

    story = []

    # Recorremos los registros en orden ascendente de fecha
    for registro in registros.order_by('created_date'):
        fecha = registro.created_date.strftime('%Y-%m-%d %H:%M')
        # Construyo un párrafo con HTML básico: fecha en negrita + descripción
        texto = (
            f"<b>{fecha} — {registro.get_emotion_display()}</b><br/>"
            f"{registro.description_day.replace('\n', '<br/>')}"
        )
        p = Paragraph(texto, normal)
        story.append(p)
        story.append(Spacer(1, 0.2 * inch))  # espacio antes del siguiente

    # Construyo el PDF
    doc.build(story)

    buffer.seek(0)
    return buffer
