from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User

class RecordingEmotion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    EMOTIONS_CHOICES = [
        ('feliz', '😊 Feliz'),
        ('agradecido', '🙏 Agradecido'),
        ('emocionado', '🤩 Emocionado'),
        ('relajado', '😌 Relajado'),
        ('normal', '😐 Normal'),
        ('contento', '😃 Contento'),
        ('triste', '😢 Triste'),
        ('enojado', '😠 Enojado'),
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
        update_slug = False

        # Si es una instancia nueva o el slug está vacío, se genera el slug.
        if not self.pk or not self.slug:
            update_slug = True
        else:
            # Compara la emoción original con la actual
            orig = RecordingEmotion.objects.get(pk=self.pk)
            if orig.emotion != self.emotion:
                update_slug = True

        if update_slug:
            current_time = timezone.now()
            base_slug = f"{self.emotion}-{current_time.strftime('%Y-%m-%d')}"
            new_slug = slugify(base_slug)
            counter = 1
            # Excluimos la instancia actual en la verificación para evitar conflictos
            while RecordingEmotion.objects.filter(slug=new_slug).exclude(pk=self.pk).exists():
                new_slug = f"{slugify(base_slug)}-{counter}"
                counter += 1
            self.slug = new_slug
                
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['-created_date']
        verbose_name = "Registro Emocional"
        verbose_name_plural = "Registros Emocionales"