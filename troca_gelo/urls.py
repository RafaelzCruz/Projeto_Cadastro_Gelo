from django.urls import path
from .views import (
    TrocaGeloCreateView,
    TrocaGeloListView,
    TrocaGeloDetailView,
    troca_gelo_sucesso
)

urlpatterns = [
    path('', TrocaGeloCreateView.as_view(), name='troca_gelo_form'),
    path('sucesso/', troca_gelo_sucesso, name='troca_gelo_sucesso'),
    path('lista/', TrocaGeloListView.as_view(), name='troca_gelo_lista'),
    path('detalhe/<int:pk>/', TrocaGeloDetailView.as_view(), name='troca_gelo_detalhe'),
]