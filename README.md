# Sistema de Vendas - Django
 
Um sistema completo de gerenciamento de vendas desenvolvido em Django, com funcionalidades para cadastro de clientes, produtos e controle de vendas.

## Funcionalidades

- **Dashboard** com visão geral do sistema
- **Gestão de Clientes** - cadastro e visualização
- **Gestão de Produtos** - cadastro e visualização
- **Controle de Vendas** - registro e acompanhamento
- **Interface moderna** com Bootstrap 5
- **Painel administrativo** completo
- **Dados de teste** incluídos

## Tecnologias Utilizadas
 
- **Backend**: Django 3.2
- **Banco de Dados**: SQLite3
- **Frontend**: Bootstrap 5 + Font Awesome
- **Linguagem**: Python 3.x

## Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

## Instalação

1. **Clone o repositório** (se aplicável) ou navegue até a pasta do projeto:
   ```bash
   cd exemplo_django
   ```

2. **Instale as dependências**:
   ```bash
   pip install django
   ```

3. **Execute as migrações**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Carregue os dados de teste**:
   ```bash
   python manage.py loaddata vendas/fixtures/dados_teste.json
   ```

5. **Crie um superusuário** (opcional):
   ```bash
   python manage.py createsuperuser
   ```

6. **Execute o servidor**:
   ```bash
   python manage.py runserver
   ```

7. **Acesse o sistema**:
   - **Sistema principal**: http://127.0.0.1:8000/
   - **Painel admin**: http://127.0.0.1:8000/admin/

## Estrutura do Banco de Dados

### Modelos

- **Cliente**: nome, email, data de cadastro
- **Produto**: nome, valor, data de cadastro
- **Venda**: cliente, produtos (relacionamento many-to-many), data/hora, valor total
- **ItemVenda**: venda, produto, quantidade, valor unitário (tabela intermediária)

### Relacionamentos

- Uma venda pertence a um cliente
- Uma venda pode ter vários produtos através da tabela ItemVenda
- Cada item de venda registra quantidade e valor unitário

## Como Usar

### 1. Dashboard
- Acesse a página inicial para ver estatísticas gerais
- Visualize totais de clientes, produtos e vendas
- Acompanhe vendas recentes

### 2. Gestão de Clientes
- Visualize todos os clientes cadastrados
- Acesse através do menu "Clientes"

### 3. Gestão de Produtos
- Visualize todos os produtos cadastrados
- Cadastre novos produtos através do botão "Novo Produto"
- Acesse através do menu "Produtos"

### 4. Controle de Vendas
- Visualize todas as vendas registradas
- Acesse detalhes de cada venda
- Acesse através do menu "Vendas"

### 5. Painel Administrativo
- Gerencie todos os dados através do Django Admin
- Acesse através do menu "Admin" ou diretamente em `/admin/`

## Estrutura do Projeto

```
exemplo_django/
├── vendas_project/          # Configurações do projeto
│   ├── settings.py         # Configurações Django
│   ├── urls.py            # URLs principais
│   └── wsgi.py            # Configuração WSGI
├── vendas/                 # Aplicação principal
│   ├── models.py          # Modelos de dados
│   ├── views.py           # Lógica de negócio
│   ├── forms.py           # Formulários
│   ├── admin.py           # Configuração do admin
│   ├── urls.py            # URLs da aplicação
│   ├── templates/         # Templates HTML
│   │   └── vendas/
│   │       ├── base.html          # Template base
│   │       ├── home.html          # Página inicial
│   │       ├── cliente_list.html  # Lista de clientes
│   │       ├── produto_list.html  # Lista de produtos
│   │       ├── produto_form.html  # Formulário de produto
│   │       ├── venda_list.html    # Lista de vendas
│   │       └── venda_detail.html  # Detalhes da venda
│   └── fixtures/          # Dados de teste
│       └── dados_teste.json
├── manage.py              # Script de gerenciamento Django
└── README.md              # Este arquivo
```

## Dados de Teste

O sistema inclui dados de teste pré-cadastrados:

- **5 clientes** com nomes e emails
- **6 produtos** de informática com valores variados
- **5 vendas** com diferentes combinações de produtos
- **8 itens de venda** distribuídos entre as vendas

## Acesso ao Sistema

### Usuário Padrão (se não criar superusuário)
- **URL**: http://127.0.0.1:8000/
- **Funcionalidades**: Visualização de dados

### Superusuário (recomendado)
- **URL**: http://127.0.0.1:8000/admin/
- **Funcionalidades**: Gerenciamento completo de todos os dados

## Personalização

- **Templates**: Edite os arquivos HTML em `vendas/templates/vendas/`
- **Estilos**: Modifique o CSS inline ou adicione arquivos CSS externos
- **Funcionalidades**: Adicione novas views em `vendas/views.py`

## Solução de Problemas

### Erro de migração
```bash
python manage.py makemigrations vendas
python manage.py migrate
```

### Erro de dados de teste
```bash
python manage.py flush  # Limpa o banco
python manage.py loaddata vendas/fixtures/dados_teste.json
```

### Erro de dependências
```bash
pip install -r requirements.txt  # Se existir
# Ou instale manualmente:
pip install django
```
## Autor

Victor Hugo Zainote
