from rest_framework import serializers
from .models import Venda


class VendaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Venda
        fields = '__all__'

    def validate_cliente(self, value):
        if not value:
            raise serializers.ValidationError(
                "Cliente é obrigatório"
            )
        return value
    def validate_produto(self, value):
        if not value:
            raise serializers.ValidationError(
                "Produto é obrigatório"
            )
        return value
    def validate_quantidade(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Quantidade deve ser maior que zero"
            )
        return value
    def validate_preco_total(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Preço total deve ser maior que zero"
            )
        return value
    def validate_data_venda(self, value):
        if not value:
            raise serializers.ValidationError(
                "Data da venda é obrigatória"
            )
        return value
    