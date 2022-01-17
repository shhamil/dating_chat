import math
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.db.models.expressions import RawSQL
from decimal import Decimal
from .utils import get_unical_name


class LocationManager(UserManager):
    def get_nearby(self, latitude, longitude, proximity, id):
        self_user = Client.objects.get(id=id)
        proximity = Decimal(proximity)
        cos_rad = Decimal(abs(math.cos(math.radians(latitude))*111.0))
        lon1 = longitude - proximity / cos_rad
        lon2 = longitude + proximity / cos_rad
        lat1 = latitude - proximity / Decimal(111.0)
        lat2 = latitude + proximity / Decimal(111.0)
        return Client.objects.filter(latitude__range=(lat1, lat2)).filter(longitude__range=(lon1, lon2)).exclude(id=id)


class Client(AbstractUser):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    objects = LocationManager()
    avatar = models.ImageField(null=True, upload_to=get_unical_name)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    surname = models.CharField(max_length=100)
    liking = models.ManyToManyField('self', through='Liker', related_name='likers', symmetrical=False)
    latitude = models.DecimalField(max_digits=10, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['latitude']),
            models.Index(fields=['longitude']),
        ]


class Liker(models.Model):
    user_from = models.ForeignKey(Client, related_name='rel_from_set', on_delete=models.CASCADE)
    user_to = models.ForeignKey(Client, related_name="rel_to_set", on_delete=models.CASCADE)

    def __str__(self):
        return '{} likes {}'.format(self.user_from, self.user_to)
