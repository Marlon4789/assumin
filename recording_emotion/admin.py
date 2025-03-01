from django.contrib import admin
from .models import RecordingEmotion

@admin.register(RecordingEmotion)
class RecordingEmotionAdmin(admin.ModelAdmin):
    list_display = ('get_emotion_display', 'created_date', 'updated', 'slug')
    list_filter = ('emotion', 'created_date')
    search_fields = ('description_day', 'discovery')
    readonly_fields = ('created_date', 'updated', 'slug')
    fieldsets = (
        ('Información emocional', {
            'fields': ('emotion', 'description_day', 'discovery')
        }),
        ('Información del sistema', {
            'fields': ('created_date', 'updated', 'slug'),
            'classes': ('collapse',)
        }),
    )
