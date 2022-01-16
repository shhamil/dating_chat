from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FormParser, MultiPartParser
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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
