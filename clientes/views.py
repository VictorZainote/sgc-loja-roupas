from produtos.models import Produto
from produtos.serializers import ProdutoSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .services.viacep import buscar_cep

from .models import Cliente
from .serializers import ClienteSerializer

from vendas.models import Venda


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]

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
    @action(detail=False, methods=["get"])
    def consultar_cep(self, request):

        cep = request.query_params.get("cep")

        if not cep:

            return Response(
                {
                    "erro": "CEP não informado"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        resultado = buscar_cep(cep)

        if not resultado:

            return Response(
                {
                    "erro": "CEP não encontrado"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(resultado)