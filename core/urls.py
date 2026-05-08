from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import home
from produtos.views import ProdutoViewSet
from clientes.views import ClienteViewSet
from vendas.views import VendaViewSet
from vendas.views import relatorio_vendas

router = DefaultRouter()

router.register(r'produtos', ProdutoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'vendas', VendaViewSet)

urlpatterns = [
    path('', home),
    
    path('admin/', admin.site.urls),

    path('', include(router.urls)),

    path(
        'relatorios/vendas/',
        relatorio_vendas
    ),
]