from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from unittest.mock import patch


class ApiAuthTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="admin",
            password="senha-teste"
        )

    def test_api_rejeita_requisicao_sem_login(self):
        response = self.client.get("/api/clientes/")

        self.assertEqual(response.status_code, 401)

    def test_api_aceita_requisicao_com_jwt(self):
        token_response = self.client.post("/api/token/", {
            "username": "admin",
            "password": "senha-teste",
        })
        access_token = token_response.data["access"]

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
        response = self.client.get("/api/clientes/")

        self.assertEqual(response.status_code, 200)

    @patch("clientes.views.buscar_cep")
    def test_consulta_cep_nao_exige_login(self, mock_buscar_cep):
        mock_buscar_cep.return_value = {
            "rua": "Praca da Se",
            "bairro": "Se",
            "cidade": "Sao Paulo",
            "estado": "SP",
        }

        response = self.client.get("/api/clientes/consultar_cep/?cep=01001000")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["cidade"], "Sao Paulo")
