import ollama
import numpy as np

def gerar_embeddings(texto, modelo="llama3.2"):
    """
    Gera embeddings para um texto usando Ollama com Llama3.2
    
    Args:
        texto (str): Texto para gerar embeddings
        modelo (str): Modelo a ser usado (padrão: 'llama3.2')
    
    Returns:
        dict: Dicionário com embeddings e informações
    """
    try:
        # Gera os embeddings
        resultado = ollama.embeddings(model=modelo, prompt=texto)
        
        # Extrai o vetor de embeddings
        embeddings = resultado["embedding"]
        
        return {
            "texto": texto,
            "modelo": modelo,
            "tamanho_vetor": len(embeddings),
            "embeddings": embeddings,
            "exemplo_valores": embeddings[:5]  # Mostra os 5 primeiros valores
        }
    except Exception as e:
        print(f"Erro ao gerar embeddings: {e}")
        return None

if __name__ == "__main__":
    # Texto de exemplo
    texto_exemplo = "Ollama se mostra como uma plataforma bem legal para rodar LLMs localmente"
    
    # Gerar embeddings
    resultado = gerar_embeddings(texto_exemplo)
    
    if resultado:
        print("\n=== Resultado dos Embeddings ===")
        print(f"Texto: {resultado['texto']}")
        print(f"Modelo usado: {resultado['modelo']}")
        print(f"Tamanho do vetor de embeddings: {resultado['tamanho_vetor']}")
        print(f"Primeiros 5 valores: {resultado['exemplo_valores']}\n")
        
        # Opcional: Salvar em um arquivo
        with open("embeddings.txt", "w") as f:
            f.write(str(resultado))
        print("Embeddings salvos em 'embeddings.txt'")