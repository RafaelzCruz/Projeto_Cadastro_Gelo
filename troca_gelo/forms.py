from django import forms
from django.core.exceptions import ValidationError
from .models import TrocaGelo

class TrocaGeloForm(forms.ModelForm):
    class Meta:
        model = TrocaGelo
        fields = [
            'modelo_caixa',
            'numero_pedido',
            'data_embalagem',
            'foto_etiqueta',
            'foto_temperatura_medicamento',
            'temperatura_medicamento',
            'foto_temperatura_gelo',
            'temperatura_gelo',
        ]
        widgets = {
            'modelo_caixa': forms.Select(attrs={
                'class': 'mt-1 block w-full rounded-lg border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 text-base py-3 px-4',
                'required': True,
            }),
            'numero_pedido': forms.TextInput(attrs={
                'class': 'mt-1 block w-full rounded-lg border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 text-base py-3 px-4',
                'placeholder': 'Ex: PED-2026-001',
                'required': True,
            }),
            'data_embalagem': forms.DateInput(attrs={
                'type': 'date',
                'class': 'mt-1 block w-full rounded-lg border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 text-base py-3 px-4',
                'required': True,
            }),
            'foto_etiqueta': forms.FileInput(attrs={
                'class': 'mt-1 block w-full text-sm text-gray-500 file:mr-4 file:py-3 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100 cursor-pointer',
                'accept': 'image/*',
                'capture': 'environment',
                'required': True,
            }),
            'foto_temperatura_medicamento': forms.FileInput(attrs={
                'class': 'mt-1 block w-full text-sm text-gray-500 file:mr-4 file:py-3 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100 cursor-pointer',
                'accept': 'image/*',
                'capture': 'environment',
                'required': True,
            }),
            'temperatura_medicamento': forms.NumberInput(attrs={
                'class': 'mt-1 block w-full rounded-lg border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 text-base py-3 px-4',
                'step': '0.1',
                'placeholder': 'Ex: 5.0',
                'required': True,
            }),
            'foto_temperatura_gelo': forms.FileInput(attrs={
                'class': 'mt-1 block w-full text-sm text-gray-500 file:mr-4 file:py-3 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100 cursor-pointer',
                'accept': 'image/*',
                'capture': 'environment',
                'required': True,
            }),
            'temperatura_gelo': forms.NumberInput(attrs={
                'class': 'mt-1 block w-full rounded-lg border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 text-base py-3 px-4',
                'step': '0.1',
                'placeholder': 'Ex: -7.0',
                'required': True,
            }),
        }
        labels = {
            'modelo_caixa': 'Passo 01: Modelo da Caixa',
            'numero_pedido': 'Passo 02: Número do Pedido',
            'data_embalagem': 'Passo 03: Data da Embalagem',
            'foto_etiqueta': 'Passo 04: Foto da Etiqueta',
            'foto_temperatura_medicamento': 'Passo 05: Foto da Temperatura do Medicamento',
            'temperatura_medicamento': 'Temperatura do Medicamento (°C)',
            'foto_temperatura_gelo': 'Passo 06: Foto da Temperatura do Gelo',
            'temperatura_gelo': 'Temperatura do Gelo (°C)',
        }
        help_texts = {
            'temperatura_medicamento': 'Faixa padrão: 2°C até 8°C (Caixa 33L: 15°C até 25°C)',
            'temperatura_gelo': 'Faixa obrigatória: -5,0°C até -9,0°C',
        }
    
    def clean_temperatura_medicamento(self):
        temp = self.cleaned_data.get('temperatura_medicamento')
        modelo = self.cleaned_data.get('modelo_caixa')
        
        if temp is None:
            raise ValidationError('Por favor, informe a temperatura do medicamento.')
        
        if modelo == '33L_IF1050':
            if not (15 <= temp <= 25):
                raise ValidationError(
                    f'Para caixa de 33 litros, a temperatura deve estar entre 15°C e 25°C. '
                    f'Temperatura informada: {temp}°C'
                )
        else:
            if not (2 <= temp <= 8):
                raise ValidationError(
                    f'A temperatura do medicamento deve estar entre 2°C e 8°C. '
                    f'Temperatura informada: {temp}°C'
                )
        
        return temp
    
    def clean_temperatura_gelo(self):
        temp = self.cleaned_data.get('temperatura_gelo')
        
        if temp is None:
            raise ValidationError('Por favor, informe a temperatura do gelo.')
        
        if not (-9 <= temp <= -5):
            raise ValidationError(
                f'A temperatura do gelo deve estar entre -5,0°C e -9,0°C. '
                f'Temperatura informada: {temp}°C'
            )
        
        return temp
    
    def clean_foto_etiqueta(self):
        foto = self.cleaned_data.get('foto_etiqueta')
        if foto:
            if foto.size > 10 * 1024 * 1024:  # 10MB
                raise ValidationError('A imagem não pode ser maior que 10MB.')
        return foto
    
    def clean_foto_temperatura_medicamento(self):
        foto = self.cleaned_data.get('foto_temperatura_medicamento')
        if foto:
            if foto.size > 10 * 1024 * 1024:  # 10MB
                raise ValidationError('A imagem não pode ser maior que 10MB.')
        return foto
    
    def clean_foto_temperatura_gelo(self):
        foto = self.cleaned_data.get('foto_temperatura_gelo')
        if foto:
            if foto.size > 10 * 1024 * 1024:  # 10MB
                raise ValidationError('A imagem não pode ser maior que 10MB.')
        return foto