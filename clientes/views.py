from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Cliente
from .serializers import ClienteSerializer

from vendas.models import Venda


class ClienteViewSet(viewsets.ModelViewSet):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def destroy(self, request, *args, **kwargs):

        cliente = self.get_object()

        possui_vendas = Venda.objects.filter(
            cliente=cliente
        ).exists()

        if possui_vendas:

            return Response(
                {
                    "erro": (
                        "Cliente possui vendas registradas"
                    )
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().destroy(
            request,
            *args,
            **kwargs
        )