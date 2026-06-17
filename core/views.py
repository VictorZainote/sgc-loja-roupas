from django.shortcuts import render
from produtos.models import Produto
from clientes.models import Cliente
from vendas.models import Venda
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request):
    return Response({
        "sistema": "SGC Loja de Roupas",
        "versao": "1.0",
        "clientes": "/api/clientes/",
        "produtos": "/api/produtos/",
        "vendas": "/api/vendas/",
    })
def home(request):
    context = {
        "total_produtos": Produto.objects.count(),
        "total_clientes": Cliente.objects.count(),
        "total_vendas": Venda.objects.count(),
    }

    return render(request, "home.html", context)