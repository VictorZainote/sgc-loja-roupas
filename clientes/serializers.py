from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'

    def validate_email(self, value):
        if Cliente.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "Email já cadastrado"
            )
        return value

    def validate_cpf(self, value):
        if Cliente.objects.filter(cpf=value).exists():
            raise serializers.ValidationError(
                "CPF já cadastrado"
            )
        return value
    def validate_nome(self, value):
        if not value:
            raise serializers.ValidationError(
                "Nome do cliente é obrigatório"
            )
        return value
        