# analysis/urls.py
from django.urls import path
from .views import SWOTListView, SWOTDetailView

urlpatterns = [
    path('', SWOTListView.as_view(), name='swot_list'),
    path('<int:pk>/', SWOTDetailView.as_view(), name='swot_detail'),
]