import requests

def buscar_cep(cep):
    cep = cep.replace("-", "").strip()

    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            return None

        dados = response.json()

        if "erro" in dados:
            return None

        return {
            "rua": dados.get("logradouro"),
            "bairro": dados.get("bairro"),
            "cidade": dados.get("localidade"),
            "estado": dados.get("uf")
        }

    except:
        return None