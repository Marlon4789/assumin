from django.shortcuts import render
from new_ideas.models import AddNewIdeas
from new_ideas.forms import AddNewIdeasForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView

# Create your views here.

class NewIdeasListView(LoginRequiredMixin, ListView):
    model = AddNewIdeas
    template_name = 'new_ideas/list.html'
    context_object_name = 'ideas'
    login_url = 'login'  # URL a la que redirige si no está autenticado

    def get_queryset(self):
        return AddNewIdeas.objects.filter(user=self.request.user).order_by('created_date')
    
class NewIdeasCreateView(LoginRequiredMixin, CreateView):
    model = AddNewIdeas
    form_class = AddNewIdeasForm
    template_name = 'new_ideas/create.html'
    # fields = ['idea']
    success_url = '/new_ideas/list'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        # Generar slug aquí también (opcional, dado que lo hace save())
        if not form.instance.slug:
            form.instance.slug = slugify(f"{self.request.user.username}-{form.instance.idea[:50]}")
        return super().form_valid(form)
    
class NewIdeasDetailView(LoginRequiredMixin, DetailView):
    model = AddNewIdeas
    template_name = 'new_ideas/detail.html'
    context_object_name = 'idea'
    slug_url_kwarg = 'slug'
    login_url = 'login'

class NewIdeasUpdateView(LoginRequiredMixin, UpdateView):
    model = AddNewIdeas
    template_name = 'new_ideas/edit.html'
    fields = ['idea']
    context_object_name = 'idea'
    slug_url_kwarg = 'slug'
    login_url = 'login'
    
    def get_success_url(self):
        return reverse_lazy('new_ideas_detail', kwargs={'slug': self.object.slug})

class NewIdeasDeleteView(LoginRequiredMixin, DeleteView):
    model = AddNewIdeas
    template_name = 'new_ideas/delete.html'
    context_object_name = 'idea'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('new_ideas_list')
    login_url = 'login'