## Sobre entrega del hito 5

* Descargar el archivo "VIGIFIA.zip" del hito 5, descomprimirlo y abrir la carpeta "VIGIFIA".
* Seguir las instrucciones que están en el README.md del hito 4.

### Documentación de nueva API a utilizar: Text embeddings de OPENAI.
* Agregada a la sección [servicios](https://github.com/ElGatoIlluminati/GRUPO10-2024-PROYINF/wiki/servicios) de la wiki.

### Implementación de API (A modo de prueba)

#### **Procesar_pdf.py**
* Este programa extrae el texto de un archivo pdf que se encuentra en algún direcotiro, y los guarda, con el fin de que sean filtrados por la API de text embedding.
* **IMPORTANTE**: Los archivos pdfs a los que se le realizará embedding deben estár en el directorio */Dir_actual/pdfs*. Donde "Dir_actual" contiene a los archivos Embedding.py y Procesar_pdf.py.

#### Embedding.py
* Este código realiza el procesamiento de documentos en formato PDF para encontrar los más relevantes según keywords. Lo anterior se hace de la siguiente forma:
  
  * Configuración de la api: Se establece la clave de la api para utilizar el modelo de text embedding.
  * Procesar pdfs: Se utiliza el archivo Porcesar_pdf.py como modulo importado.
  * Obtención del embedding:
    * get_embedding(): Llama a la API para generar un embedding de un texto dado.
    * crear_embeddings() crea los embeddings para los documentos de un directorio.
      
  * Similitud coseno:
    * similitud_coseno(): Calcula qué tan parecidos son dos vectores, utilizando la fórmula coseno, midiendo su cercanía en un espacio multidimensional.
  * Búsqueda de documentos relevantes
    * buscar_relevantes(): Toma una query, calcula el embedding y, posteriormente, la   similitud coseno entre el embedding de la query y el de los documentos.
    * Los documentos se ordenan en de mayor a menor relevancia.
 
#### Aspectos a considerar
La utilización de la API mencionada tiene un costo monetario, en forma de tokens, para la utilización de esta, por lo tanto, no fue posible hacer pruebas exhaustivas del funcionamiento.

### [Video Resultado Final](https://youtu.be/CVS0R8VaA-E)

