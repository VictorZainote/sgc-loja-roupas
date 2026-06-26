from rest_framework import serializers

from .models import Venda


class VendaSerializer(serializers.ModelSerializer):
    cliente_nome = serializers.CharField(source="cliente.nome", read_only=True)
    produto_nome = serializers.CharField(source="produto.nome", read_only=True)

    class Meta:
        model = Venda
        fields = '__all__'
        read_only_fields = ("valor_total", "data_venda")

    def validate_cliente(self, value):
        if not value:
            raise serializers.ValidationError("Cliente e obrigatorio")

        return value

    def validate_produto(self, value):
        if not value:
            raise serializers.ValidationError("Produto e obrigatorio")

        return value

    def validate_quantidade(self, value):
        if value <= 0:
            raise serializers.ValidationError("Quantidade deve ser maior que zero")

        return value

    def validate(self, attrs):
        produto = attrs.get("produto", self.instance.produto if self.instance else None)
        quantidade = attrs.get("quantidade", self.instance.quantidade if self.instance else None)

        if produto and quantidade:
            estoque_disponivel = produto.quantidade_estoque

            if self.instance and self.instance.produto_id == produto.id:
                estoque_disponivel += self.instance.quantidade

            if estoque_disponivel < quantidade:
                raise serializers.ValidationError({
                    "quantidade": "Estoque insuficiente para esta venda"
                })

        return attrs
