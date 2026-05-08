from django.test import TestCase

from produtos.models import Produto
from clientes.models import Cliente
from .models import Venda


class VendaTestCase(TestCase):

    def setUp(self):

        self.produto = Produto.objects.create(
            nome='Tênis',
            preco=200,
            quantidade_estoque=5,
            categoria='Calçados'
        )

        self.cliente = Cliente.objects.create(
            nome='Victor',
            email='victor@email.com',
            telefone='61999999999'
        )

    def test_registrar_venda(self):

        venda = Venda.objects.create(
            cliente=self.cliente,
            produto=self.produto,
            quantidade=2,
            valor_total=0
        )

        self.produto.refresh_from_db()

        self.assertEqual(
            self.produto.quantidade_estoque,
            3
        )

        self.assertEqual(
            venda.valor_total,
            400
        )

    def test_estoque_insuficiente(self):

        with self.assertRaises(ValueError):

            Venda.objects.create(
                cliente=self.cliente,
                produto=self.produto,
                quantidade=10,
                valor_total=0
            )