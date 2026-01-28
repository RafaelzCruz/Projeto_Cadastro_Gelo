from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from .models import TrocaGelo
from .forms import TrocaGeloForm

class TrocaGeloCreateView(CreateView):
    """View para criar nova troca de gelo"""
    model = TrocaGelo
    form_class = TrocaGeloForm
    template_name = 'troca_gelo/formulario.html'
    success_url = reverse_lazy('troca_gelo_sucesso')
    
    def form_valid(self, form):
        # Adiciona o usuário se estiver autenticado
        if self.request.user.is_authenticated:
            form.instance.usuario = self.request.user.username
        
        messages.success(
            self.request,
            'Formulário de Troca de Gelo registrado com sucesso! '
            'Você pode iniciar um novo registro.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(
            self.request,
            'Por favor, corrija os erros abaixo e tente novamente.'
        )
        return super().form_invalid(form)


class TrocaGeloListView(ListView):
    """View para listar todas as trocas de gelo"""
    model = TrocaGelo
    template_name = 'troca_gelo/lista.html'
    context_object_name = 'trocas'
    paginate_by = 20
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Filtros opcionais
        modelo = self.request.GET.get('modelo')
        if modelo:
            queryset = queryset.filter(modelo_caixa=modelo)
        
        data_inicio = self.request.GET.get('data_inicio')
        data_fim = self.request.GET.get('data_fim')
        if data_inicio and data_fim:
            queryset = queryset.filter(
                data_embalagem__range=[data_inicio, data_fim]
            )
        
        return queryset


class TrocaGeloDetailView(DetailView):
    """View para ver detalhes de uma troca de gelo"""
    model = TrocaGelo
    template_name = 'troca_gelo/detalhe.html'
    context_object_name = 'troca'


def troca_gelo_sucesso(request):
    """Página de sucesso após registrar troca"""
    return render(request, 'troca_gelo/sucesso.html')