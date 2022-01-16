from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import get_unical_name


class Client(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    avatar = models.ImageField(null=True, upload_to=get_unical_name)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    surname = models.CharField(max_length=100)
