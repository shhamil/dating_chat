from django.urls import path, include
from .views import UserRegistrationView

app_name = 'dating_chat'

urlpatterns = [
    path('api/clients/create', UserRegistrationView.as_view(), name='registration'),
]
