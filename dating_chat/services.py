from .models import Client
import django_filters


class ClientFilter(django_filters.FilterSet):
    gender = django_filters.CharFilter()
    first_name = django_filters.CharFilter()
    surname = django_filters.CharFilter()
    distance = django_filters.NumberFilter()

    class Meta:
        model = Client
        fields = ['gender', 'first_name', 'surname', 'distance']

    def filter_queryset(self, queryset):
        if 'distance' in self.request.GET and self.request.GET['distance'] is not None:
            queryset = Client.objects.get_nearby(self.request.user.latitude, self.request.user.longitude, self.request.GET['distance'], self.request.user.id)
        return queryset.exclude(id=self.request.user.id)
