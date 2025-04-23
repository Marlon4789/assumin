from django.urls import path
from .views import (
    RecordingListView, 
    RecordingCreateView, 
    RecordingDetailView,
    RecordingUpdateView,
    RecordingDeleteView,
    NewUserWelcomeView,
)

urlpatterns = [
    path('', RecordingListView.as_view(), name='registro_lista'),
    path('nuevo/', RecordingCreateView.as_view(), name='registro_nuevo'),
    path('detalle/<slug:slug>/', RecordingDetailView.as_view(), name='registro_detalle'),
    path('editar/<slug:slug>/', RecordingUpdateView.as_view(), name='registro_editar'),
    path('eliminar/<slug:slug>/', RecordingDeleteView.as_view(), name='registro_eliminar'),
    path('bienvenido/', NewUserWelcomeView.as_view(), name='new_user_welcome'),
]