# Projeto de Geolocalização

Este é um projeto backend API Django para gerenciamento de alvos (geolocalização).


### Clone o repositório:

    git clone https://github.com/MykleBR/Join-Tecnologia.git


## Configuração do Ambiente

    Crie e ative um ambiente virtual:

        python -m venv venv
        Para Linux/Mac = source venv/bin/activate
        Para Windows = .\venv\Scripts\activate


### Instale as dependências:
        pip install -r requirements.txt


### Configuração do Banco de Dados

        Configure as credenciais do banco de dados em settings.py.

        Execute as migrações:
            python manage.py migrate


### Inicie o servidor Django:
        python manage.py runserver


O servidor estará disponível em http://localhost:8000/.

### Endpoints da API:

        /api/alvos/                         : Lista todos os alvos.
        /api/alvos/<int:alvo_id>/           : Detalhes de um alvo específico.
        /api/alvos/cria/                    : Cria um novo alvo.
        /api/alvos/atualiza/<int:alvo_id>/  : Atualiza um alvo existente.
        /api/alvos/exclui/<int:alvo_id>/    : Exclui um alvo existente.


Exemplos de Uso


### Criar um Novo Alvo - POS
    {"nome": "Novo Alvo", "latitude": 10123, "longitude": -45.678} 
    http://localhost:8000/api/alvos/cria/


### Listar Alvos - GET
    http://localhost:8000/api/alvos/


### Detalhes de um Alvo - GET
    http://localhost:8000/api/alvos/1/


### Atualizar um Alvo - PUT
    {"nome": "Alvo Atualizado", "latitude": 11.456, "longitude": -46.789} 
    http://localhost:8000/api/alvos/atualiza/1/


### Excluir um Alvo - POST
    http://localhost:8000/api/alvos/exclui/1/