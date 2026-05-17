from django.test import TestCase
from clientes.services.viacep import buscar_cep


class ViaCepTestCase(TestCase):

    def test_buscar_cep(self):

        resultado = buscar_cep("01001000")

        self.assertIsNotNone(resultado)
        self.assertEqual(resultado["cidade"], "São Paulo")
        self.assertEqual(resultado["estado"], "SP")