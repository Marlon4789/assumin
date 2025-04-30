from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class AddNewIdeas(models.Model):
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    idea         = models.TextField("¿Cuál es tu idea?", blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated      = models.DateTimeField(auto_now=True)
    slug         = models.SlugField(unique=True)   # ¡No blank=True, obligatorio!

    def save(self, *args, **kwargs):
        # Si no tiene slug, créalo a partir de la idea y la fecha
        if not self.slug:
            base = self.idea[:50] if self.idea else str(self.created_date.timestamp())
            self.slug = slugify(f"{self.user.username}-{base}")
        super().save(*args, **kwargs)
