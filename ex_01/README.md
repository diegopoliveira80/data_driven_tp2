# Aplicação FastAPI com GPT-2

Este projeto implementa uma API de chatbot utilizando FastAPI e o modelo GPT-2 da biblioteca Transformers. A aplicação está organizada em módulos.

## Documentação
Swagger UI: http://127.0.0.1:8000/docs

## Pré-requisitos
Certifique-se de ter as seguintes ferramentas instaladas:

- **Python 3.8 ou superior**
- arquivo requirements.txt

## Execultar aplicacao
1° Clone o repositório
2° Crie e ative um ambiente virtual
3° Instale as dependências requirements.txt
4° Inicie o servidor com o Uvicorn
    uvicorn main:app
5° Execulte um POST para aplicação
    http POST http://localhost:8000/chat/message/ message=""


## Estrutura do Projeto

```plaintext
EX_01/
│
├── main.py              # Aplicação principal FastAPI
├── gpt2/
│   ├── routers/
│   │   └── chat.py      # Roteador para o endpoint de chat
│   └── models/
│       └── chat.py      # Modelo Pydantic para validação de entrada
├── requirements.txt     # Lista de dependências
└── README.md            # Instruções de uso
