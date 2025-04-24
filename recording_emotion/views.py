from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import RecordingEmotion
from .forms import RecordingEmotionForm

class RecordingListView(LoginRequiredMixin, ListView):
    model = RecordingEmotion
    template_name = 'recording_emotion/lista.html'
    context_object_name = 'registros'
    login_url = 'login'  # URL a la que redirige si no está autenticado

    def get_queryset(self):
        return RecordingEmotion.objects.filter(user=self.request.user).order_by('created_date')


class RecordingCreateView(LoginRequiredMixin, CreateView):
    model = RecordingEmotion
    form_class = RecordingEmotionForm
    template_name = 'recording_emotion/crear.html'
    success_url = reverse_lazy('registro_lista')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user  # Asigna el usuario que está logueado
        return super().form_valid(form)

class RecordingDetailView(LoginRequiredMixin, DetailView):
    model = RecordingEmotion
    template_name = 'recording_emotion/detalle.html'
    context_object_name = 'registro'
    slug_url_kwarg = 'slug'
    login_url = 'login'

class RecordingUpdateView(LoginRequiredMixin, UpdateView):
    model = RecordingEmotion
    form_class = RecordingEmotionForm
    template_name = 'recording_emotion/editar.html'
    context_object_name = 'registro'
    slug_url_kwarg = 'slug'
    login_url = 'login'
    
    def get_success_url(self):
        return reverse_lazy('registro_detalle', kwargs={'slug': self.object.slug})

class RecordingDeleteView(LoginRequiredMixin, DeleteView):
    model = RecordingEmotion
    template_name = 'recording_emotion/eliminar.html'
    context_object_name = 'registro'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('registro_lista')
    login_url = 'login'


class NewUserWelcomeView(LoginRequiredMixin, TemplateView):
    template_name = 'recording_emotion/new_user_welcome.html'
    login_url = 'login'