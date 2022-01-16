from django.urls import path, include
from .views import UserRegistrationView, UserSympathyView

app_name = 'dating_chat'

urlpatterns = [
    path('api/clients/create', UserRegistrationView.as_view(), name='registration'),
    path('api/clients/<int:id>/match', UserSympathyView.as_view(), name='sympa'),
]
