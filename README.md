# Geração de Embeddings com Ollama e Llama3.2

Este projeto tem pretenção de demonstrar como gerar vetores de embeddings usando Ollama com o modelo Llama3.2 localmente.

## Pré-requisitos
- Python 3.13 instalado e configurado na máquina local
Disponível em: https://www.python.org/downloads/

- Ollama instalado localmente
Disponível em: https://ollama.com/download

- Modelo Llama3.2 instalado localmente (via `ollama run llama3.2`)

- Para verificar se o Ollama e o llama3.2 estão de fato instalados, no terminal digite:
    `ollama list`

## Instalação

1. Clone este repositório:

   git clone https://github.com/1l2pf/tarefa3.git
   cd tarefa3

2. Crie um ambiente virtual   

    python -m venv tarefa3
    tarefa3\Scripts\activate

3. Instale as dependencias (via `pip install -r requirements.txt`)

4. Execute o seguinte script: `python gerar_embeddings.py`

5. Ao final será gerado um arquivo embeddings.txt com os embeddings gerados. 