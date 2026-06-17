from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Venda
from .serializers import VendaSerializer


class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    permission_classes = [IsAuthenticated]
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer


@api_view(['GET'])
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