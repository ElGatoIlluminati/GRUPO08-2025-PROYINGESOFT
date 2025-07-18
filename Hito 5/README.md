
# Proyecto VigiFIA - Hito 5: Versión Final

## Tecnologías Utilizadas

- **Backend:** Python 3.11, Django 5.2
- **Base de Datos:** PostgreSQL 15
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Editor de Contenido:** Django Summernote (Editor WYSIWYG)
- **Contenerización:** Docker y Docker Compose

---

## Guía de Instalación y Ejecución Local

Siga estos pasos en orden para levantar el proyecto. Se asume que tiene **Docker Desktop** instalado y en ejecución.

### 1. Clonar el Repositorio

Primero, clonar este repositorio en la máquina local y navegar a la carpeta correcta.

```bash
# Clonar el repositorio desde GitHub
git clone https://github.com/ElGatoIlluminati/GRUPO08-2025-PROYINGESOFT.git

# Navegar a la carpeta del Hito 5
cd "GRUPO08-2025-PROYINGESOFT/Hito 5/"
````

### 2\. Configurar las Variables de Entorno

El proyecto necesita un archivo `.env` para cargar las credenciales y configuraciones. Se incluyó una plantilla para facilitar el proceso.

```bash
# En Windows (usando PowerShell), Mac o Linux
cp .env.example .env
```

> **Nota:** No se necesita modificar este archivo. Los valores por defecto están diseñados para funcionar con la configuración de Docker Compose, por lo cual solo se debe cambiar el nombre de .env.example por .env

### 3\. Construir y Levantar los Contenedores

Ahora, se leerá el archivo `docker-compose.yml`, construirá la imagen de Python/Django con todas las dependencias y levantará los servicios de la aplicación (`web`) y la base de datos (`db`).

```bash
docker-compose up --build -d
```

  - `--build`: Fuerza la reconstrucción de la imagen para asegurar que se usen las últimas versiones de los archivos.
  - `-d`: (Detached mode) Ejecuta los contenedores en segundo plano, dejando su terminal libre.

### 4\. Preparar la Base de Datos

Con los contenedores ya corriendo, se necesita inicializar la base de datos.

1.  **Aplicar Migraciones:** Este comando crea toda la estructura de tablas que Django necesita.

    ```bash
    docker-compose exec web python manage.py makemigrations django_summernote
    docker-compose exec web python manage.py migrate
    ```

2.  **Crear un Superusuario (Opcional, pero recomendado):** Para tener acceso total al panel de administración de Django, se puede crear una cuenta propia de superusuario.

    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

    Seguir las instrucciones en pantalla para elegir un nombre de usuario, correo y contraseña.

3.  **Cargar Datos de Prueba:** Este es el paso más importante. Ejecutar el script que crea los usuarios, categorías y boletines de ejemplo.

    ```bash
    docker-compose exec web python manage.py crear_usuarios_prueba
    ```

4.  **Cargar el sitio:** Carga la página (En caso de no funcionar en el primero intento, presionar Ctrl + C e intentar nuevamente)

    ```bash
    docker-compose up
    ```

### 5\. Final

Ahora la aplicación ya está completamente funcional.

  - **Acceder a la Página Web:** Abrir el navegador e ir a **[http://localhost:8000](https://www.google.com/search?q=http://localhost:8000)**
  - **Acceder al Panel de Administración:** Se puede ir a **[http://localhost:8000/admin/](https://www.google.com/search?q=http://localhost:8000/admin/)** y usar las credenciales del superusuario que se crearon en el paso anterior.

### Credenciales de Acceso (Usuarios de Prueba)

Para facilitar la revisión, se pueden usar las siguientes cuentas pre-cargadas en la página de "Iniciar Sesión":

| Rol | Usuario | Contraseña |
| :--- | :--- | :--- |
| **Administrador** | `admin` | `admin123` |
| **Editor** | `editor` | `editor123` |
| **Lector** | `lector` | `lector123` |

El usuario Administrador tiene rol de admin, y los otros 2 usuarios por defecto son lectores, además debería haber pre-cargados 2 boletines de prueba, pero por alguna razón no se almaceno la foto ni el archivo, por lo cual hay que modificar el boletin y subir una nueva foto y pdf.
Otro dato importante, el admin tiene su propio panel para crear etiquetas y otorgar roles a los usuarios

-----

### Cómo Detener la Aplicación

Cuando se haya terminado de revisar, se pueden detener todos los servicios de Docker con el siguiente comando:

```bash
docker-compose down
```

> **Nota:** Si se desea borrar también la base de datos para empezar de cero la próxima vez, se debe usar:

```bash
docker-compose down -v
```
