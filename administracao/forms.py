from django import forms
from django.forms import widgets
from .models import Servico
from decimal import Decimal

class ServicoForm(forms.ModelForm):
    valor_minimo = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    porcentagem_comissao = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    valor_quarto = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    valor_sala = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    valor_banheiro = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    valor_quintal = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    valor_cozinha = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    valor_outros = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))

    class Meta:
        model = Servico
        fields = '__all__'

    def clean_valor_minumo(self):
        data = self.cleaned_data['valor_minimo']
        return Decimal(data.replace(',','.'))