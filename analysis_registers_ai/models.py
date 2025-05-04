from django.db import models
from django.contrib.auth.models import User

class SWOTAnalysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    period_start   = models.DateField()
    period_end     = models.DateField()
    analysis       = models.TextField(blank=True)        # <-- nuevo
    positive_patterns = models.JSONField(default=list)   # <-- nuevo
    negative_patterns = models.JSONField(default=list)   # <-- nuevo
    strengths      = models.TextField()
    weaknesses     = models.TextField()
    opportunities  = models.TextField()
    threats        = models.TextField()
    recommendations = models.TextField(blank=True)       # <-- nuevo
    previous       = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    processed_count= models.PositiveIntegerField(default=0)
    created_at     = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Análisis DOFA'
        verbose_name_plural = 'Análisis DOFA'

    def __str__(self):
        return f"DOFA {self.period_start} – {self.period_end} ({self.user.username})"
