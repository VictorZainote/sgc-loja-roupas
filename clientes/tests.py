from django.test import TestCase

from .models import Cliente


class ClienteTestCase(TestCase):

    def test_criar_cliente(self):

        cliente = Cliente.objects.create(
            nome='Victor',
            email='victor@email.com',
            telefone='61999999999'
        )

        self.assertEqual(
            cliente.nome,
            'Victor'
        )