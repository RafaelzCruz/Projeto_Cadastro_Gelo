from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from datetime import timedelta

class CaixaModelo(models.Model):
    """Modelos de caixas disponíveis"""
    MODELOS_CHOICES = [
        ('12L_IF2000', '12 litros IF-2.000 / 02 unidades gelox ice foam 2.000'),
        ('12L_IT1050', '12 litros IT-1050 / 03 unidades gelox ita fria 1050'),
        ('33L_IF1050', '33 litros IF-1050 PRECAUÇÃO / 01 unidade gelox Ice Foam-1050'),
        ('44L_IT1050', '44 litros IT-1050 / 06 unidades gelox Ita Fria 1050'),
        ('80L_IT1050', '80 litros IT-1050 / 10 unidades gelox Ita Fria 1050'),
        ('120L_IT1050', '120 litros IT-1050 / 12 unidades gelox Ita Fria 1050'),
    ]
    
    nome = models.CharField(max_length=20, choices=MODELOS_CHOICES, unique=True)
    litros = models.IntegerField()
    unidades_gelox = models.IntegerField()
    tipo_gelox = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Modelo de Caixa'
        verbose_name_plural = 'Modelos de Caixas'
    
    def __str__(self):
        return dict(self.MODELOS_CHOICES)[self.nome]


class TrocaGelo(models.Model):
    """Registro de troca de gelo 5S"""
    
    # Passo 01
    modelo_caixa = models.CharField(
        max_length=20,
        choices=CaixaModelo.MODELOS_CHOICES,
        verbose_name='Modelo da Caixa'
    )
    
    # Passo 02
    numero_pedido = models.CharField(
        max_length=50,
        verbose_name='Número do Pedido da Caixa'
    )
    
    # Passo 03
    data_embalagem = models.DateField(
        verbose_name='Data da Embalagem da Caixa'
    )
    
    # Passo 04
    foto_etiqueta = models.ImageField(
        upload_to='trocas_gelo/etiquetas/%Y/%m/%d/',
        verbose_name='Foto da Etiqueta da Caixa'
    )
    
    # Passo 05
    foto_temperatura_medicamento = models.ImageField(
        upload_to='trocas_gelo/temp_medicamento/%Y/%m/%d/',
        verbose_name='Foto da Temperatura do Medicamento'
    )
    temperatura_medicamento = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        validators=[MinValueValidator(-50), MaxValueValidator(50)],
        verbose_name='Temperatura do Medicamento (°C)'
    )
    
    # Passo 06
    foto_temperatura_gelo = models.ImageField(
        upload_to='trocas_gelo/temp_gelo/%Y/%m/%d/',
        verbose_name='Foto da Temperatura do Gelo'
    )
    temperatura_gelo = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        validators=[MinValueValidator(-50), MaxValueValidator(50)],
        verbose_name='Temperatura do Gelo (°C)'
    )
    
    # Campos de ambientação (calculados automaticamente)
    hora_finalizacao = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Hora de Finalização'
    )
    hora_inicio_ambientacao = models.DateTimeField(
        verbose_name='Início da Ambientação',
        editable=False
    )
    
    # Campos de controle
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    usuario = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Troca de Gelo 5S'
        verbose_name_plural = 'Trocas de Gelo 5S'
        ordering = ['-criado_em']
    
    def save(self, *args, **kwargs):
        # Calcula automaticamente o horário de início da ambientação (20 minutos antes)
        if not self.hora_inicio_ambientacao:
            # Se hora_finalizacao ainda não foi definida (primeiro save), usa o horário atual
            horario_referencia = self.hora_finalizacao or timezone.now()
            self.hora_inicio_ambientacao = horario_referencia - timedelta(minutes=20)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Troca {self.numero_pedido} - {self.get_modelo_caixa_display()} - {self.criado_em.strftime('%d/%m/%Y %H:%M')}"
    
    def validar_temperatura_medicamento(self):
        """Valida se a temperatura do medicamento está na faixa correta"""
        if self.modelo_caixa == '33L_IF1050':
            # Caixa de 33 litros: 15°C até 25°C
            return 15 <= self.temperatura_medicamento <= 25
        else:
            # Outras caixas: 2°C até 8°C
            return 2 <= self.temperatura_medicamento <= 8
    
    def validar_temperatura_gelo(self):
        """Valida se a temperatura do gelo está na faixa correta"""
        # Todas as caixas: -5°C até -9°C
        return -9 <= self.temperatura_gelo <= -5
    
    @property
    def temperaturas_validas(self):
        """Retorna True se ambas as temperaturas estão válidas"""
        return self.validar_temperatura_medicamento() and self.validar_temperatura_gelo()
    
    @property
    def faixa_temperatura_medicamento(self):
        """Retorna a faixa de temperatura esperada para o medicamento"""
        if self.modelo_caixa == '33L_IF1050':
            return "15°C até 25°C"
        return "2°C até 8°C"