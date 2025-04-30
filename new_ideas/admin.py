from django.contrib import admin
from .models import AddNewIdeas

@admin.register(AddNewIdeas)
class AddNewIdeasAdmin(admin.ModelAdmin):
    # Campos que aparezcan en la lista de objetos
    list_display = ('user', 'idea', 'created_date', 'updated', 'slug')
    # Campos de búsqueda
    search_fields = ('idea', 'user__username')
    # Filtros laterales
    list_filter  = ('created_date', 'user')
    # Si quieres que el slug se autogenere al escribir la idea:
    prepopulated_fields = {'slug': ('idea',)}
    # Orden por defecto
    ordering = ('-created_date',)

