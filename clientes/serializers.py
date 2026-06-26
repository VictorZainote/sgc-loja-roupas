from rest_framework import serializers

from .models import Cliente


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'

    def validate_email(self, value):
        queryset = Cliente.objects.filter(email=value)

        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError("Email ja cadastrado")

        return value

    def validate_nome(self, value):
        if not value:
            raise serializers.ValidationError("Nome do cliente e obrigatorio")

        return value
