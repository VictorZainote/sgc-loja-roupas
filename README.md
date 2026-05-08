# SGC - Sistema de Gestão Comercial

## Descrição

Sistema de Gestão Comercial desenvolvido para uma loja de roupas utilizando Django e Django REST Framework.

O sistema permite gerenciamento de clientes, produtos, vendas, controle de estoque e relatórios, seguindo princípios de organização em APIs REST.

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
- Testes automatizados básicos

---

## Tecnologias Utilizadas

- Python
- Django
- Django REST Framework
- SQLite
- HTML/CSS
- Git e GitHub

---

## Estrutura do Projeto

```txt
clientes/
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

### Criar ambiente virtual

```bash
python -m venv venv
```

### Ativar ambiente virtual

```bash
venv\Scripts\activate
```

### Instalar dependências

```bash
pip install django djangorestframework
```

### Rodar migrations

```bash
python manage.py migrate
```

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

### API Produtos

```txt
http://127.0.0.1:8000/api/produtos/
```

### API Clientes

```txt
http://127.0.0.1:8000/api/clientes/
```

### API Vendas

```txt
http://127.0.0.1:8000/api/vendas/
```

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