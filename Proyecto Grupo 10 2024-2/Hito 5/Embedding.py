import openai
import numpy as np
from scipy.spatial.distance import cosine
import Procesar_pdf
import os

# Configura tu clave de API de OpenAI
openai.api_key = "CLAVE_PROPIO_DE_OPENAI"

cargar_documentos = Procesar_pdf.cargar_documentos
extraer_texto = Procesar_pdf.extraer_texto

# Función para obtener el embedding de un texto usando, OpenAI
def get_embedding(text):
    """Obtiene el embedding de un texto usando OpenAI."""
    # Llama a la API de OpenAI para obtener el embedding
    response = openai.embeddings.create(  
        model="text-embedding-ada-002",  # Modelo recomendado para embeddings
        input=text  # El texto que se va a procesar
    )
    # Devuelve el embedding del primer resultado
    return response['data'][0]['embedding'] 

# Función que crea embeddings para todos los documentos en un diccionario
def crear_embeddings(documents):
    embeddings = {}
    
    for filename, content in documents.items():
        embeddings[filename] = get_embedding(content)
    return embeddings

# Función para calcular la similitud coseno entre dos vectores
def similitud_coseno(vec1, vec2):
    # Convierte los vectores a arrays de NumPy
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    # Calcula la similitud coseno entre los dos vectores
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

# Función que busca los documentos más relevantes a partir de una consulta
def find_most_relevant_documents(query, document_embeddings):

    # Se obtiene el embedding para la consulta (query)
    query_embedding = get_embedding(query)
    similarities = {}
    
    # Compara la similitud coseno entre el embedding de la consulta y los embeddings de los documentos
    for filename, doc_embedding in document_embeddings.items():
        similarity = similitud_coseno(query_embedding, doc_embedding)
        similarities[filename] = similarity
    
    # Ordena los documentos por su relevancia
    sorted_docs = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
    return sorted_docs

directorio_actual = os.path.dirname(os.path.abspath(__file__))

directory_path = os.path.join(directorio_actual, "pdfs")

documents = cargar_documentos(directory_path)

document_embeddings = crear_embeddings(documents)

keywords = "agricultura sostenible" # Este input será cambiado por el que hace el administador de VIGIFIA.
relevant_documents = find_most_relevant_documents(keywords, document_embeddings)

# Mostrar los resultados
print("Documentos más relevantes para la consulta:")
for filename, score in relevant_documents:
    print(f"{filename}: {score}")
