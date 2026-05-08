from django.test import TestCase

from .models import Produto


class ProdutoTestCase(TestCase):

    def test_criar_produto(self):

        produto = Produto.objects.create(
            nome='Camiseta',
            preco=99.90,
            quantidade_estoque=10,
            categoria='Roupas'
        )

        self.assertEqual(
            produto.nome,
            'Camiseta'
        )

        self.assertEqual(
            produto.quantidade_estoque,
            10
        )