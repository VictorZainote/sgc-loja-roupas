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

from .views import (
    api_root,
    cep_page,
    clientes_page,
    home,
    login_page,
    produtos_page,
    vendas_page,
)

router = DefaultRouter()

router.register(r'produtos', ProdutoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'vendas', VendaViewSet)

urlpatterns = [

    path('', home, name='home'),
    path('login/', login_page, name='login'),
    path('clientes/', clientes_page, name='clientes_page'),
    path('produtos/', produtos_page, name='produtos_page'),
    path('vendas/', vendas_page, name='vendas_page'),
    path('cep/', cep_page, name='cep_page'),

    path('admin/', admin.site.urls),

    path('api/info/', api_root, name='api_info'),
    path('api/', include(router.urls)),

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
