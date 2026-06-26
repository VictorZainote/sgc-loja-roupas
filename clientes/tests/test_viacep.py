from unittest.mock import Mock, patch

from django.test import TestCase

from clientes.services.viacep import buscar_cep


class ViaCepTestCase(TestCase):

    @patch("clientes.services.viacep.requests.get")
    def test_buscar_cep(self, mock_get):
        response = Mock()
        response.json.return_value = {
            "logradouro": "Praca da Se",
            "bairro": "Se",
            "localidade": "Sao Paulo",
            "uf": "SP",
        }
        response.raise_for_status.return_value = None
        mock_get.return_value = response

        resultado = buscar_cep("01001000")

        self.assertEqual(resultado["rua"], "Praca da Se")
        self.assertEqual(resultado["cidade"], "Sao Paulo")
        self.assertEqual(resultado["estado"], "SP")
        mock_get.assert_called_once_with(
            "https://viacep.com.br/ws/01001000/json/",
            timeout=5
        )
