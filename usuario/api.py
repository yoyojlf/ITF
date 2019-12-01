from django.http import HttpResponse
from django.views.generic import View
from rest_framework.response import Response
from rest_framework.views import APIView

from usuario.models import Usuario, TipoUsuario
from usuario.serializers import UserSerializer, TipoUserSerializer
from rest_framework.renderers import JSONRenderer


class UserListAPI(APIView):

    def get(self, request):
        users = Usuario.objects.all()
        serializer = UserSerializer(users, many=True)
        serializer_users = serializer.data
        ##renderer = JSONRenderer()
        ##json_users = renderer.render(serializer_users) # lista de disccionarios a json
        ##return HttpResponse(json_users)
        return Response(serializer_users)

class TipoUserListAPI(APIView):

    def get(self, request):
        t_users = TipoUsuario.objects.all()
        serializer = TipoUserSerializer(t_users, many=True)
        serializer_users = serializer.data
        ##renderer = JSONRenderer()
        ##json_users = renderer.render(serializer_users) # lista de disccionarios a json
        ##return HttpResponse(json_users)
        return Response(serializer_users)
