from django.contrib import admin
from .models import TrocaGelo, CaixaModelo

@admin.register(CaixaModelo)
class CaixaModeloAdmin(admin.ModelAdmin):
    list_display = ['nome', 'litros', 'unidades_gelox', 'tipo_gelox']
    search_fields = ['nome', 'tipo_gelox']


@admin.register(TrocaGelo)
class TrocaGeloAdmin(admin.ModelAdmin):
    list_display = [
        'numero_pedido',
        'modelo_caixa',
        'data_embalagem',
        'temperatura_medicamento',
        'temperatura_gelo',
        'status_temperaturas',
        'criado_em',
    ]
    list_filter = [
        'modelo_caixa',
        'data_embalagem',
        'criado_em',
    ]
    search_fields = [
        'numero_pedido',
        'usuario',
    ]
    readonly_fields = [
        'hora_inicio_ambientacao',
        'hora_finalizacao',
        'criado_em',
        'atualizado_em',
    ]
    fieldsets = (
        ('Informações da Caixa', {
            'fields': ('modelo_caixa', 'numero_pedido', 'data_embalagem')
        }),
        ('Fotos', {
            'fields': ('foto_etiqueta', 'foto_temperatura_medicamento', 'foto_temperatura_gelo')
        }),
        ('Temperaturas', {
            'fields': ('temperatura_medicamento', 'temperatura_gelo')
        }),
        ('Período de Ambientação', {
            'fields': ('hora_inicio_ambientacao', 'hora_finalizacao')
        }),
        ('Informações do Sistema', {
            'fields': ('usuario', 'criado_em', 'atualizado_em'),
            'classes': ('collapse',)
        }),
    )
    
    def status_temperaturas(self, obj):
        """Exibe status visual das temperaturas"""
        if obj.temperaturas_validas:
            return "✅ Conforme"
        return "❌ Fora da faixa"
    status_temperaturas.short_description = 'Status'
    
    def get_readonly_fields(self, request, obj=None):
        """Define campos readonly baseado no contexto"""
        if obj:  # Editando objeto existente
            return self.readonly_fields + ('modelo_caixa',)
        return self.readonly_fields