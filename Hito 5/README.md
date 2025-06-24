````md
# Proyecto VigiFIA - Hito 5: Versión Final

## 🛠️ Tecnologías Utilizadas

- **Backend:** Python 3.11, Django 5.2
- **Base de Datos:** PostgreSQL 15
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Editor de Contenido:** Django Summernote (Editor WYSIWYG)
- **Contenerización:** Docker y Docker Compose

---

## 🚀 Guía de Instalación y Ejecución Local

Siga estos pasos en orden para levantar el proyecto. Se asume que tiene **Docker Desktop** instalado y en ejecución.

### 1. Clonar el Repositorio

Primero, clone este repositorio en su máquina local y navegue a la carpeta correcta.

```bash
# Clone el repositorio desde GitHub
git clone [https://github.com/ElGatoIlluminati/GRUPO08-2025-PROYINGESOFT.git](https://github.com/ElGatoIlluminati/GRUPO08-2025-PROYINGESOFT.git)

# Navegue a la carpeta del Hito 5
cd GRUPO08-2025-PROYINGESOFT/Hito\ 5/
````

### 2\. Configurar las Variables de Entorno

El proyecto necesita un archivo `.env` para cargar las credenciales y configuraciones. Hemos incluido una plantilla para facilitar este proceso.

```bash
# En Windows (usando PowerShell)
cp .env.example .env

# En Mac o Linux
cp .env.example .env
```

> **Nota:** No necesita modificar este archivo. Los valores por defecto están diseñados para funcionar con la configuración de Docker Compose.

### 3\. Construir y Levantar los Contenedores

Ahora, se leerá el archivo `docker-compose.yml`, construirá la imagen de Python/Django con todas las dependencias y levantará los servicios de la aplicación (`web`) y la base de datos (`db`).

```bash
docker-compose up --build -d
```

  - `--build`: Fuerza la reconstrucción de la imagen para asegurar que se usen las últimas versiones de los archivos.
  - `-d`: (Detached mode) Ejecuta los contenedores en segundo plano, dejando su terminal libre.

### 4\. Preparar la Base de Datos

Con los contenedores ya corriendo, necesitamos inicializar la base de datos.

1.  **Aplicar Migraciones:** Este comando crea toda la estructura de tablas que Django necesita.

    ```bash
    docker-compose exec web python manage.py migrate
    ```

2.  **Crear un Superusuario (Opcional, pero recomendado):** Para tener acceso total al panel de administración de Django, es una buena idea crear su propia cuenta de superusuario.

    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

    Siga las instrucciones en pantalla para elegir un nombre de usuario, correo y contraseña.

3.  **Cargar Datos de Prueba:** Este comando utiliza el archivo `initial_data.json` para poblar la base de datos con usuarios, categorías y boletines de ejemplo, permitiendo una revisión inmediata de la funcionalidad.

    ```bash
    docker-compose exec web python manage.py loaddata initial_data.json
    ```

### 5\. ¡Proyecto Listo\!

Ahora la aplicación ya está completamente funcional.

  - **Acceder a la Página Web:** Abra su navegador y vaya a 👉 **[http://localhost:8000](https://www.google.com/search?q=http://localhost:8000)**
  - **Acceder al Panel de Administración:** Puede ir a 👉 **[http://localhost:8000/admin/](https://www.google.com/search?q=http://localhost:8000/admin/)** y usar las credenciales del superusuario que creó en el paso anterior.

### 🔑 Credenciales de Acceso (Usuarios de Prueba)

Para facilitar la revisión, puede usar las siguientes cuentas pre-cargadas en la página de "Iniciar Sesión":

| Rol | Usuario | Contraseña |
| :--- | :--- | :--- |
| 🧑‍💻 **Administrador** | `admin` | `admin123` |
| ✍️ **Editor** | `editor` | `editor123` |
| 📖 **Lector** | `lector` | `lector123` |

-----

### 🛑 Cómo Detener la Aplicación

Cuando haya terminado de revisar, puede detener todos los servicios de Docker con el siguiente comando:

```bash
docker-compose down
```

> **Nota:** Si desea borrar también la base de datos para empezar de cero la próxima vez, use `docker-compose down -v`.

```
```