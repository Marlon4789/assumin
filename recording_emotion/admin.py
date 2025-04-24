# recording_emotion/admin.py

from django.contrib import admin
from django.http import FileResponse

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import RecordingEmotion
from .utils.pdf import generate_registros_pdf



@admin.register(RecordingEmotion)
class RecordingEmotionAdmin(admin.ModelAdmin):
    list_display    = ('user', 'get_emotion_display', 'created_date')
    list_filter     = ('emotion', 'created_date')
    search_fields   = ('description_day', 'discovery')
    readonly_fields = ('created_date', 'updated', 'slug')
    fieldsets       = (
        ('Información emocional', {
            'fields': ('emotion', 'description_day', 'discovery'),
        }),
        ('Información del sistema', {
            'fields': ('created_date', 'updated', 'slug'),
            'classes': ('collapse',),
        }),
    )

    # 1) Indica que hay una acción disponible
    actions = ['exportar_pdf']

    # 2) Define el método DENTRO de la clase
    def exportar_pdf(self, request, queryset):
        """
        Acción de admin para generar un PDF con los registros seleccionados,
        ordenados por fecha ascendente.
        """
        buffer = generate_registros_pdf(queryset)
        return FileResponse(buffer, as_attachment=True, filename='registros.pdf')
    exportar_pdf.short_description = "Exportar registros seleccionados a PDF"

