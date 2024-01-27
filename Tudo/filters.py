import django_filters
from models import Tudo


class TudoFilter(django_filters.FilterSet):
    start_total = django_filters.NumberFilter(field_name='total', lookup_expr='gt')
    end_total = django_filters.NumberFilter(field_name='total', lookup_expr='lt')

    class Meta:
        model = Tudo
        fields = ['start_total', 'end_total']