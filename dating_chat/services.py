from .models import Client
import django_filters


class ClientFilter(django_filters.FilterSet):
    gender = django_filters.CharFilter()
    first_name = django_filters.CharFilter()
    surname = django_filters.CharFilter()

    class Meta:
        model = Client
        fields = ['gender', 'first_name', 'surname']
