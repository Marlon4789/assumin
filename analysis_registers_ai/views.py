# analysis/views.py
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import SWOTAnalysis

class SWOTListView(LoginRequiredMixin, ListView):
    model = SWOTAnalysis
    template_name = 'analysis/list.html'
    context_object_name = 'analyses'

    def get_queryset(self):
        return SWOTAnalysis.objects.filter(user=self.request.user)

class SWOTDetailView(LoginRequiredMixin, DetailView):
    model = SWOTAnalysis
    template_name = 'analysis/detail.html'
    context_object_name = 'analysis'