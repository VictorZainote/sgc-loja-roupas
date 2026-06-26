from rest_framework import serializers

from .models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

    def validate_preco(self, value):
        if value <= 0:
            raise serializers.ValidationError("Preco deve ser maior que zero")

        return value

    def validate_quantidade_estoque(self, value):
        if value < 0:
            raise serializers.ValidationError("Estoque nao pode ser negativo")

        return value

    def validate_nome(self, value):
        if not value:
            raise serializers.ValidationError("Nome do produto e obrigatorio")

        return value
