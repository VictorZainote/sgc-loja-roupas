from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from produtos.views import ProdutoViewSet
from clientes.views import ClienteViewSet
from vendas.views import (
    VendaViewSet,
    relatorio_vendas
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import api_root, home

router = DefaultRouter()

router.register(r'produtos', ProdutoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'vendas', VendaViewSet)

urlpatterns = [

    path('', home),

    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),
    
    path('api/', api_root),

    path(
        'relatorios/vendas/',
        relatorio_vendas
    ),
    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'api-auth/',
        include('rest_framework.urls')
    ),
]