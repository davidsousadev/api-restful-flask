# API RESTful - Flask

Esta é uma API RESTful construída com Flask e SQLAlchemy para gerenciar um conjunto de itens. A API permite operações de CRUD (Create, Read, Update, Delete) em itens armazenados em um banco de dados SQLite.

## Funcionalidades

- **Criar um novo item**: POST /items
- **Listar todos os itens**: GET /items
- **Obter um item específico**: GET /items/<int:item_id>
- **Atualizar um item existente**: PUT /items/<int:item_id>
- **Deletar um item**: DELETE /items/<int:item_id>

## Tecnologias Utilizadas

- Python
- Flask
- SQLAlchemy
- SQLite

## Estrutura do Projeto

- app.py: Arquivo principal que contém a definição da API.
- models.py: Define os modelos de dados e inicializa o banco de dados.
- instance/items.db: Banco de dados SQL em arquivo.

## Instalação

### 1. Clone o repositório:
   
```sh

   git clone https://github.com/davidsousadev/api-restful-flask.git
   cd api-restful-flask

```
### 2. Crie um ambiente virtual e ative-o (Opcional):

```sh

python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

```

### 3. Instale as dependências:

```sh

pip install -r requirements.txt

```

### 4. Inicie o servidor:
```sh

flask run

```
Ou
```sh

python app.py

```

A API estará disponível em http://127.0.0.1:5000/items.

## Endpoints

- **POST /items** - Cria um novo item.

Requisição

```sh

curl -X POST http://127.0.0.1:5000/items \
     -H "Content-Type: application/json" \
     -d '{"item": "Item 1"}'

```

Resposta

```

{
  "id": 1,
  "item": "Item 1"
}

```

- **GET /items** - Retorna uma lista de todos os itens.

Requisição

```sh

curl -X GET http://127.0.0.1:5000/items \
    -H "Content-Type: application/json"

```

Resposta

```

[
  {
    "id": 1,
    "item": "Item 1"
  }
]

```
- **GET /items/int:item_id** - Retorna os detalhes de um item específico.

Requisição

```sh

curl -X GET http://127.0.0.1:5000/items/1 \
    -H "Content-Type: application/json" 

```

Resposta

```

{
  "id": 1,
  "item": "Item 1"
}

```

- **PUT /items/int:item_id** - Atualiza um item existente.

Requisição

```sh

curl -X PUT http://127.0.0.1:5000/items/1 \
    -H "Content-Type: application/json" \
    -d '{"item": "Item Atualizado!"}'

```

Resposta

```

{
  "id": 1,
  "item": "Item Atualizado"
}

```
- **DELETE /items/int:item_id** - Deleta um item específico.

Requisição

```sh

curl -X DELETE http://127.0.0.1:5000/items/1 \
    -H "Content-Type: application/json"

```

Resposta

```


```