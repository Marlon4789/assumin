from django.urls import path
from .views import (
    NewIdeasListView, 
    NewIdeasCreateView, 
    NewIdeasDetailView,
    NewIdeasUpdateView,
    NewIdeasDeleteView,
)
urlpatterns = [
    path('list/', NewIdeasListView.as_view(), name='new_ideas_list'),
    path('', NewIdeasCreateView.as_view(), name='new_ideas_create'),
    path('detail/<slug:slug>/', NewIdeasDetailView.as_view(), name='new_ideas_detail'),
    path('edit/<slug:slug>/', NewIdeasUpdateView.as_view(), name='new_ideas_edit'),
    path('delete/<slug:slug>/', NewIdeasDeleteView.as_view(), name='new_ideas_delete'),
]