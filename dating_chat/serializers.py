from rest_framework import serializers
from .models import Client


class ClientRegistrationSerializer(serializers.ModelSerializer):


    class Meta:
        model = Client
        fields = ('username', 'first_name', 'surname', 'avatar', 'gender', 'email', 'password', 'latitude', 'longitude')


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('username', 'first_name', 'surname', 'gender', 'avatar')
