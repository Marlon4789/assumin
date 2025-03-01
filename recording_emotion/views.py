from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import RecordingEmotion
from .forms import RecordingEmotionForm

class RecordingListView(ListView):
    model = RecordingEmotion
    template_name = 'recording_emotion/lista.html'
    context_object_name = 'registros'

    def get_queryset(self):
        return RecordingEmotion.objects.order_by('created_date')

class RecordingCreateView(CreateView):
    model = RecordingEmotion
    form_class = RecordingEmotionForm
    template_name = 'recording_emotion/crear.html'
    success_url = reverse_lazy('registro_lista')

class RecordingDetailView(DetailView):
    model = RecordingEmotion
    template_name = 'recording_emotion/detalle.html'
    context_object_name = 'registro'
    slug_url_kwarg = 'slug'

class RecordingUpdateView(UpdateView):
    model = RecordingEmotion
    form_class = RecordingEmotionForm
    template_name = 'recording_emotion/editar.html'
    context_object_name = 'registro'
    slug_url_kwarg = 'slug'
    
    def get_success_url(self):
        return reverse_lazy('registro_detalle', kwargs={'slug': self.object.slug})

class RecordingDeleteView(DeleteView):
    model = RecordingEmotion
    template_name = 'recording_emotion/eliminar.html'
    context_object_name = 'registro'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('registro_lista')