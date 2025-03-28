import os  
import PyPDF2  

# Función para extraer el texto de un archivo PDF
def extraer_texto(pdf_path):
    # Abre el archivo PDF en modo lectura binaria
    with open(pdf_path, 'rb') as pdf_file:
        # Crea un objeto lector de PDF
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""  # Cadena vacía para almacenar el texto extraído
        # Itera sobre todas las páginas del PDF
        for page in reader.pages:
            text += page.extract_text()  # Extrae el texto de cada página
        return text  # Retorna el texto extraído

# Función para cargar todos los documentos de un directorio
def cargar_documentos(directory):
    documents = {}  # Diccionario vacío para almacenar los documentos con su contenido
    # Itera sobre todos los archivos en el directorio especificado
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):  # Filtra solo los archivos PDF
            file_path = os.path.join(directory, filename)  # Obtiene la ruta completa del archivo
            documents[filename] = extraer_texto(file_path)  # Extrae el texto del PDF y lo agrega al diccionario
    return documents  # Retorna el diccionario con los documentos y su contenido
