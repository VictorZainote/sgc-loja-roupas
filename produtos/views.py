from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Produto
from .serializers import ProdutoSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):

        try:
            return super().create(request, *args, **kwargs)

        except Exception as erro:

            return Response(
                {
                    'erro': str(erro)
                },
                status=status.HTTP_400_BAD_REQUEST
            )