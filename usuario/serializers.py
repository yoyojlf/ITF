from rest_framework import serializers
from usuario.models import Usuario, TipoUsuario

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField() # read only
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        """
        crea una istancia de user a partir de
        los datos
        de validated_data que contiene valores
        deserializados
        :param validated_data:
        :return:
        """
        instance = Usuario()
        return self.update(instance,validated_data)

    def update(self, instance, validated_data):
        """
        actualiza una instancia de user
        a partir de los datos de
        validated_data
        :param instance:
        :param validated_data:
        :return:
        """
        instance = Usuario()
        instance.first_name = validated_data.get('firts_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance

class TipoUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    description = serializers.CharField()
    is_active = serializers.BooleanField()
    def create(self, validated_data):
        """
        crea una istancia de user a partir de
        los datos
        de validated_data que contiene valores
        deserializados
        :param validated_data:
        :return:
        """
        instance = TipoUsuario()
        return self.update(instance,validated_data)

    def update(self, instance, validated_data):
        """
        actualiza una instancia de user
        a partir de los datos de
        validated_data
        :param instance:
        :param validated_data:
        :return:
        """
        instance = TipoUsuario()
        instance.name = validated_data.get('name')
        instance.description = validated_data.get('description')
        instance.is_active = validated_data.get('is_avtive')
        instance.save()
        return instance

