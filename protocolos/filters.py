import django_filters
from django import forms
from .models import Historico, Status
from django.db.models import Q

# jeito mais simples para criar consultas e personaliar a forma de comparação
class HistoricoFilter(django_filters.FilterSet):
    class Meta:
        model = Historico
        fields = {
            # Busca pelo nome do aluno (solicitado_por) da solicitação
            'solicitacao__solicitado_por__nome' : ['icontains'],            
            'status' : ['exact'],
            'gerado_em' : ['gte', 'lte'], #<= e >=
            'gerado_por' : ['exact'],
        }


# Jeito mais elaborado, criando os filtros manualmente
class HistoricoFilter2(django_filters.FilterSet):

    nome_solicitante = django_filters.CharFilter(
        label='Solicitado por', # rótulo do campo no formulário
        widget=forms.TextInput(attrs={'placeholder': 'Nome ou matrícula'}), # Adicione o placeholder no input do formulário
        method='filter_nome_ou_matricula' # método para filtar por nome ou matrícula
        # Com método personalizado não precisa especificar o field_name e o lookup_expr
    )

    status = django_filters.ModelChoiceFilter(
        field_name='status', # atributo de comparação
        queryset=Status.objects.all(), # queryset para popular o select
        label='Status' # rótulo do campo no formulário
    )

    gerado_em__gte = django_filters.DateFilter(
        field_name='gerado_em',
        lookup_expr='gte',
        label='Gerado a partir de',
        # widget permite personalizar o campo do formulário
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    gerado_em__lte = django_filters.DateFilter(
        field_name='gerado_em',
        lookup_expr='lte',
        label='Gerado até',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    
    gerado_em__year = django_filters.NumberFilter(
        field_name='gerado_em__year',
        label='Ano',
        widget=forms.NumberInput(attrs={'placeholder': 'Ano (YYYY)'})
    )


    # Método personalizado para filtrar por nome ou matrícula
    def filter_nome_ou_matricula(self, queryset, name, value):
        return queryset.filter(
            Q(solicitacao__solicitado_por__nome__icontains=value) |
            Q(solicitacao__solicitado_por__matricula__icontains=value)
        )