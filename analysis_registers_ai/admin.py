from django.contrib import admin
from .models import SWOTAnalysis

class SWOTAnalysisAdmin(admin.ModelAdmin):
    list_display = ('user', 'period_start', 'period_end', 'strengths', 'weaknesses', 'opportunities', 'threats', 'created_at', 'processed_count')
    list_filter = ('user', 'period_start', 'period_end')
    search_fields = ('user__username', 'strengths', 'weaknesses', 'opportunities', 'threats')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    readonly_fields = ('analysis','positive_patterns','negative_patterns','recommendations',
                       'strengths','weaknesses','opportunities','threats')

admin.site.register(SWOTAnalysis, SWOTAnalysisAdmin)
