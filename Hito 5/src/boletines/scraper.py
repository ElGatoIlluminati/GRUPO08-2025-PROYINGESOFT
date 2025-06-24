# src/boletines/scraper.py

import requests
from bs4 import BeautifulSoup

def fetch_agromet_data(tema):
    """
    Función encargada de hacer web scraping a las fuentes de datos.
    Recibe un 'tema' y devuelve una lista de textos encontrados.
    """
    print(f"--- Iniciando scraping para el tema: {tema} ---")

    # URL de ejemplo. En el futuro, podemos tener una lista de URLs
    # y decidir cuál usar basándonos en el 'tema'.
    URL = "https://agrometeorologia.cl/"

    scraped_data = []

    try:
        # 1. Hacemos la petición para obtener el HTML de la página
        response = requests.get(URL, timeout=10)
        response.raise_for_status()  # Esto lanzará un error si la petición falla (ej: 404)

        # 2. Parseamos el HTML con BeautifulSoup
        soup = BeautifulSoup(response.content, 'lxml')

        # 3. Buscamos y extraemos la información
        #    Esta es la parte que necesita ser personalizada.
        #    Debes "inspeccionar" la página web para encontrar las etiquetas
        #    y clases correctas que contienen la información que quieres.

        # EJEMPLO: Supongamos que las noticias están en etiquetas <article>
        # con la clase 'post-item'.
        noticias = soup.find_all('article', class_='post-item')

        print(f"Se encontraron {len(noticias)} noticias (ejemplo).")

        for noticia in noticias:
            titulo_tag = noticia.find('h2', class_='post-title')
            resumen_tag = noticia.find('div', class_='post-content')

            if titulo_tag and resumen_tag:
                titulo = titulo_tag.get_text(strip=True)
                resumen = resumen_tag.get_text(strip=True)

                # Añadimos la información encontrada a nuestra lista
                scraped_data.append(f"Título: {titulo}. Resumen: {resumen}")

        if not scraped_data:
            scraped_data.append("No se pudo extraer información estructurada, se devolverá el texto plano.")
            # Si no encontramos la estructura esperada, podríamos devolver parte del texto plano
            scraped_data.append(soup.get_text(strip=True, separator='\n')[:1000])


    except requests.exceptions.RequestException as e:
        print(f"Error al intentar acceder a la URL {URL}: {e}")
        scraped_data.append(f"Error de conexión: {e}")

    print("--- Scraping finalizado ---")
    return scraped_data