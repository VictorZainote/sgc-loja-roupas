import requests


def buscar_cep(cep):
    cep = "".join(filter(str.isdigit, cep))

    if len(cep) != 8:
        print(f"CEP invalido: {cep}")
        return None

    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        dados = response.json()

        if "erro" in dados:
            print(f"CEP nao encontrado: {cep}")
            return None

        resultado = {
            "rua": dados.get("logradouro"),
            "bairro": dados.get("bairro"),
            "cidade": dados.get("localidade"),
            "estado": dados.get("uf")
        }

        print("Dados ViaCEP:", resultado)
        return resultado

    except requests.RequestException as erro:
        print(f"Erro ao consultar ViaCEP: {erro}")
        return None
