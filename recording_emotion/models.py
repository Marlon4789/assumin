from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class RecordingEmotion(models.Model):
    EMOTIONS_CHOICES = [
        ('feliz', '😊 Feliz'),
        ('agradecido', '🙏 Agradecido'),
        ('emocionado', '🤩 Emocionado'),
        ('triste', '😢 Triste'),
        ('enojado', '😠 Enojado'),
        ('relajado', '😌 Relajado'),
        ('contento', '😃 Contento'),
        ('cansado', '😫 Cansado'),
        ('aburrido', '😒 Aburrido'),
    ]
    
    emotion = models.CharField(max_length=20, choices=EMOTIONS_CHOICES)
    description_day = models.TextField(verbose_name="Cuéntame cómo fue tu día", blank=True)
    discovery = models.CharField(max_length=300, verbose_name="¿Descubriste algo nuevo hoy?", blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    
    def __str__(self):
        return f"Registro del {self.created_date.strftime('%d/%m/%Y')} - {self.get_emotion_display()}"
    
    def save(self, *args, **kwargs):
        # Generar slug si no existe
        if not self.slug:
            # Usamos timezone.now() para tener una fecha actual
            current_time = timezone.now()
            base_slug = f"{self.emotion}-{current_time.strftime('%Y-%m-%d')}"
            self.slug = slugify(base_slug)
            
            # Asegurar que el slug sea único
            counter = 1
            while RecordingEmotion.objects.filter(slug=self.slug).exists():
                self.slug = f"{slugify(base_slug)}-{counter}"
                counter += 1
                
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['-created_date']
        verbose_name = "Registro Emocional"
        verbose_name_plural = "Registros Emocionales"