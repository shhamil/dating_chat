from django.contrib import admin
from .models import Client, Liker


@admin.register(Client)
class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'surname')
    list_filter = ('username', 'first_name', 'last_name')


admin.site.register(Liker)

