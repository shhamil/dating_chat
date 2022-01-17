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
        return Client.objects.get_nearby(self.request.user.latitude, self.request.user.longitude, self.request.GET['distance'])
