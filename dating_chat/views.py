from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail

from watermark.add_watermark import add_watermark
from .models import Client, Liker
from .serializers import ClientRegistrationSerializer


class UserRegistrationView(CreateAPIView):
    serializer_class = ClientRegistrationSerializer
    parser_classes = (FormParser, MultiPartParser)

    def post(self, *args, **kwargs):
        serializer = ClientRegistrationSerializer(data=self.request.POST)
        if serializer.is_valid():
            new_user = serializer.save()
            new_user.set_password(serializer.data['password'])
            new_user.avatar = self.request.FILES['avatar']
            new_user.save()
            add_watermark(new_user.avatar.path)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserSympathyView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        user_to = Client.objects.get(id=kwargs.get('id'))
        if user_to == self.request.user:
            return Response({'Ошибка': 'Вы итак себе нравитесь!'})
        Liker.objects.get_or_create(user_from=self.request.user, user_to=user_to)
        if user_to in self.request.user.liking.all():
            send_mail('Взаимная симпатия',
                      'Вы понравились {}! Почта участника: {}'.format(user_to.first_name, user_to.email),
                      'shkurban0595@gmail.com',
                      [self.request.user.email, ])
            send_mail('Взаимная симпатия',
                      'Вы понравились {}! Почта участника: {}'.format(self.request.user.username,
                                                                      self.request.user.email),
                      'shkurban0595@gmail.com',
                      [user_to.email, ])
            return Response({'sympathy_user_email': user_to.email}, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_201_CREATED)
