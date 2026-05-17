# SGC - Sistema de Gestão Comercial

## Deploy da Aplicação

Aplicação publicada em:

[LINK_DO_RENDER_AQUI]

---

## Descrição

Sistema de Gestão Comercial desenvolvido para uma loja de roupas utilizando Django e Django REST Framework.

O sistema permite gerenciamento de clientes, produtos, vendas, controle de estoque e relatórios, seguindo princípios de APIs REST, integração com serviços externos e testes automatizados.

---

## Funcionalidades

- Cadastro de clientes
- Edição e listagem de clientes
- Cadastro de produtos
- Controle de estoque
- Registro de vendas
- Cálculo automático do valor total da venda
- Relatórios de vendas
- Tratamento de exceções
- API REST com Django REST Framework
- Integração com API ViaCEP
- Consulta de CEP em tempo real
- Testes automatizados
- CI com GitHub Actions

---

## Integração com API Pública

O sistema possui integração com a API pública ViaCEP para consulta automática de endereços a partir do CEP informado.

### Endpoint de consulta

```txt
/api/clientes/consultar_cep/?cep=01001000
```

### Exemplo de resposta

```json
{
    "rua": "Praça da Sé",
    "bairro": "Sé",
    "cidade": "São Paulo",
    "estado": "SP"
}
```

---

## Tecnologias Utilizadas

- Python
- Django
- Django REST Framework
- SQLite
- Requests
- Pytest
- Gunicorn
- GitHub Actions
- Render
- HTML/CSS
- Git e GitHub

---

## Estrutura do Projeto

```txt
clientes/
│
├── services/
│   └── viacep.py
│
├── tests/
│   └── test_viacep.py
│
produtos/
vendas/
core/
templates/
static/
database/
```

---

## Banco de Dados

Script SQL disponível em:

```txt
/database/script.sql
```

---

## Como Executar o Projeto

### Clonar repositório

```bash
git clone https://github.com/SEU_USUARIO/sgc-loja-roupas.git
```

---

### Criar ambiente virtual

```bash
python -m venv venv
```

---

### Ativar ambiente virtual

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/macOS

```bash
source venv/bin/activate
```

---

### Instalar dependências

```bash
pip install -r requirements.txt
```

---

### Rodar migrations

```bash
python manage.py migrate
```

---

### Executar servidor

```bash
python manage.py runserver
```

---

## Executar Testes

```bash
python manage.py test
```

---

## Rotas Principais

### Home

```txt
http://127.0.0.1:8000/
```

---

### API Produtos

```txt
http://127.0.0.1:8000/api/produtos/
```

---

### API Clientes

```txt
http://127.0.0.1:8000/api/clientes/
```

---

### API Vendas

```txt
http://127.0.0.1:8000/api/vendas/
```

---

### Consulta CEP

```txt
http://127.0.0.1:8000/api/clientes/consultar_cep/?cep=01001000
```

---

## Testes Automatizados

O projeto possui testes automatizados para validar:

- integração com API ViaCEP;
- funcionamento dos endpoints;
- consistência da aplicação.

---

## CI/CD

O projeto utiliza GitHub Actions para execução automática dos testes e validação contínua da aplicação.

---

## Modelagem

O projeto contém:

- Diagrama de Domínio
- Diagrama de Classes
- Diagrama Lógico do Banco de Dados

---

## Documentação

Documentação complementar:

```txt
https://docs.google.com/document/d/1AJ8xdTkNCCYhtKbnrIHEyspB8Yrpt4DlH7d6ma2dEXI/edit?tab=t.0
```

---

## Autor

Victor Hugo Zainote