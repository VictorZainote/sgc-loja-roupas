from rest_framework import serializers, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Venda
from .serializers import VendaSerializer


class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.select_related("cliente", "produto").all()
    serializer_class = VendaSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        try:
            serializer.save()
        except ValueError as error:
            raise serializers.ValidationError({"erro": str(error)})

    def perform_update(self, serializer):
        try:
            serializer.save()
        except ValueError as error:
            raise serializers.ValidationError({"erro": str(error)})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def relatorio_vendas(request):

    data_inicio = request.GET.get('inicio')
    data_fim = request.GET.get('fim')

    vendas = Venda.objects.all()

    if data_inicio and data_fim:

        vendas = vendas.filter(
            data_venda__date__range=[
                data_inicio,
                data_fim
            ]
        )

    total_vendas = vendas.count()

    valor_total = sum(
        venda.valor_total for venda in vendas
    )

    return Response({
        'total_vendas': total_vendas,
        'valor_total': valor_total
    })
