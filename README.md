# Aplicação FastAPI com GPT-2 e haggingface(tradutor en - fr)

ex_01 - Este projeto implementa uma API de chatbot utilizando FastAPI e o modelo GPT-2 da biblioteca Transformers.
ex_02 - Este projeto implementa uma API de chatbot para tradução do EN para FR utilizando FastAPI e o modelo 
ex_03 - Este projeto implementa uma API de para simular o uso de LLM atraves do FAKE llm
ex_04 - Este projeto implementa uma API de chatbot para tradução do EN para FR utilizando FastAPI e o modelo OPENAI
ex_05 - Este projeto implementa uma API de chatbot para tradução do EN para Alemão utilizando FastAPI e o modelo Helsinki-NLP/opus-mt-en-DE da biblioteca Transformers.

## Documentação
Utilize a documentação para utilizar a forma correta de consulta
Swagger UI: http://localhost/docs

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
    http POST http://localhost:8000/"verificar Swagger"


## Estrutura do Projeto 
EX_01

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


EX_02

```plaintext
EX_02/
│
├── main.py              # Aplicação principal FastAPI
├── huggingface/
│   ├── routers/
│   │   └── chat.py      # Roteador para o endpoint de chat
│   └── models/
        └── chat.py      # Modelo Pydantic para validação de entrada


EX_03

```plaintext
EX_03/
│
├── main.py              # Aplicação principal FastAPI
├── fake_llm/
│   ├── routers/
│   │   └── chat.py      # Roteador para o endpoint de chat
│   └── models/
        └── chat.py      # Modelo Pydantic para validação de entrada



EX_04

```plaintext
EX_04/
│
├── main.py              # Aplicação principal FastAPI
│
├── routers/
│   └── chat.py      # Roteador para o endpoint de chat
└── models/
    └── chat.py      # Modelo Pydantic para validação de entrada


EX_05

```plaintext
EX_05/
│
├── main.py              # Aplicação principal FastAPI
├── huggingface/
│   ├── routers/
│   │   └── chat.py      # Roteador para o endpoint de chat
│   └── models/
        └── chat.py      # Modelo Pydantic para validação de entrada
