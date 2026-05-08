from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Venda
from .serializers import VendaSerializer


class VendaViewSet(viewsets.ModelViewSet):

    queryset = Venda.objects.all()
    serializer_class = VendaSerializer


@api_view(['GET'])
def relatorio_vendas(request):

    vendas = Venda.objects.all()

    total_vendas = vendas.count()

    valor_total = sum(
        venda.valor_total for venda in vendas
    )

    return Response({
        "total_vendas": total_vendas,
        "valor_total": valor_total
    })