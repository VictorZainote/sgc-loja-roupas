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


def login_page(request):
    return render(request, "registro/login.html")


def clientes_page(request):
    return render(request, "clientes.html")


def produtos_page(request):
    return render(request, "produtos.html")


def vendas_page(request):
    context = {
        "clientes": Cliente.objects.order_by("nome"),
        "produtos": Produto.objects.order_by("nome"),
    }
    return render(request, "vendas.html", context)


def cep_page(request):
    return render(request, "cep.html")
